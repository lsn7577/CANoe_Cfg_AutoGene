import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from workflows.canoe_auto_generation_burr.agents import capl_authoring_agent


class CaplAuthoringAgentTest(unittest.TestCase):
    def test_payload_is_scoped_to_capl_profile(self) -> None:
        payload = capl_authoring_agent.build_payload(
            {"project": {"target_canoe_version": "v12"}, "cases": []},
            {"strategy": {}},
            {"mounted_files": {"cfg": ["base.cfg"]}},
            {"pages": [{"symbol": "diagSendRequest", "description": "send diagnostic request"}]},
            {"status": "pass"},
            {
                "id": "capl_authoring",
                "profile_path": "capl_authoring.json",
                "topic_filters": ["capl"],
                "blocked_topic_filters": ["canoe_config", "cfg", "com_automation"],
            },
        )

        self.assertEqual(payload["retrieval_profile"]["id"], "capl_authoring")
        self.assertIn("com_automation", payload["retrieval_profile"]["blocked_topic_filters"])
        self.assertEqual(payload["evidence_pages"][0]["symbol"], "diagSendRequest")

    def test_call_agent_reports_unavailable_without_command(self) -> None:
        with TemporaryDirectory() as tmp, patch.dict(os.environ, {}, clear=True):
            result = capl_authoring_agent.call_agent({"schema_version": "0.1.0"}, Path(tmp))

        self.assertEqual(result["status"], "unavailable")
        self.assertIn("payload_file", result)

    def test_call_agent_accepts_valid_external_response(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "fake_agent.py"
            script.write_text(
                "\n".join([
                    "import json, sys",
                    "response = {",
                    "  'capl_source': '/* Generated for CANoe v12 */\\nvariables\\n{\\n}\\nvoid MainTest()\\n{\\n}\\n',",
                    "  'capl_script_plan': {'assumptions': [], 'adapter_gaps': [], 'used_evidence_refs': [], 'cases': []}",
                    "}",
                    "open(sys.argv[2], 'w', encoding='utf-8').write(json.dumps(response))",
                ]),
                encoding="utf-8",
            )
            command = f'"{sys.executable}" "{script}" "{{payload}}" "{{response}}"'
            with patch.dict(os.environ, {capl_authoring_agent.COMMAND_ENV: command}):
                result = capl_authoring_agent.call_agent({"schema_version": "0.1.0"}, root)

        self.assertEqual(result["status"], "generated")
        self.assertIn("capl_source", result["response"])


if __name__ == "__main__":
    unittest.main()
