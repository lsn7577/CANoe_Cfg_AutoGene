import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from workflows.canoe_auto_generation_burr.agents import claude_code_capl_agent


class ClaudeCodeCaplAgentTest(unittest.TestCase):
    def test_split_command_spec_keeps_quoted_windows_path(self) -> None:
        parts = claude_code_capl_agent._split_command_spec('"D:\\nodejs\\node_global\\claude.cmd" --debug')

        self.assertEqual(parts[0].strip('"'), "D:\\nodejs\\node_global\\claude.cmd")
        self.assertIn("--debug", parts)

    def test_build_prompt_preserves_fixer_contract(self) -> None:
        payload = {
            "role": "fixer",
            "prompt_parts": [
                {"name": "immutable_golden_ir", "replaceable": False, "content": {"cases": []}},
                {"name": "current_complete_code", "replaceable": True, "content": "variables\n{\n}\n"},
                {"name": "latest_compile_error_log", "replaceable": True, "content": "syntax error"},
            ],
            "hard_constraints": ["Do not add behavior that is absent from golden_ir."],
        }

        prompt = claude_code_capl_agent.build_prompt(payload)

        self.assertIn("You are the Fixer", prompt)
        self.assertIn("immutable_golden_ir", prompt)
        self.assertIn("latest_compile_error_log", prompt)
        self.assertIn("Return exactly one JSON object", prompt)
        self.assertIn("Generated for CANoe", prompt)
        self.assertIn("message MessageType msg_MessageType", prompt)

    def test_extract_response_from_claude_json_wrapper(self) -> None:
        stdout = json.dumps({
            "type": "result",
            "result": json.dumps({
                "golden_ir": {
                    "project": {},
                    "cases": [],
                    "capl_api_plan": [],
                    "assertions": [],
                    "branching": [],
                    "evidence_refs": [],
                }
            }),
        })

        response = claude_code_capl_agent.extract_response(stdout)

        self.assertIn("golden_ir", response)

    def test_build_claude_command_uses_plain_text_output(self) -> None:
        command = claude_code_capl_agent.build_claude_command("planner")

        output_format_index = command.index("--output-format")
        self.assertEqual(command[output_format_index + 1], "text")

    def test_run_agent_invokes_claude_and_writes_response(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            payload_path = root / "payload.json"
            response_path = root / "response.json"
            payload_path.write_text(
                json.dumps({"role": "planner", "project": {}, "cases": []}),
                encoding="utf-8",
            )
            completed = SimpleNamespace(
                returncode=0,
                stdout=json.dumps({
                    "result": json.dumps({
                        "golden_ir": {
                            "project": {},
                            "cases": [],
                            "capl_api_plan": [],
                            "assertions": [],
                            "branching": [],
                            "evidence_refs": [],
                        }
                    })
                }),
                stderr="",
            )
            with patch.dict(os.environ, {claude_code_capl_agent.CLAUDE_COMMAND_ENV: "claude"}, clear=False), patch(
                "workflows.canoe_auto_generation_burr.agents.claude_code_capl_agent.subprocess.run",
                return_value=completed,
            ) as run:
                response = claude_code_capl_agent.run_agent(payload_path, response_path)

            self.assertIn("golden_ir", response)
            self.assertEqual(json.loads(response_path.read_text(encoding="utf-8")), response)
            args, kwargs = run.call_args
            self.assertIn("--json-schema", args[0])
            self.assertIn("Payload JSON", kwargs["input"])


if __name__ == "__main__":
    unittest.main()
