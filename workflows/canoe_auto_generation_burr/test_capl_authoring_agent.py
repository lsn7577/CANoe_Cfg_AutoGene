import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from burr.core import State

from workflows.canoe_auto_generation_burr import canoe_workflow
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
            capl_authoring_agent._CONFIG_CACHE = {}
            with patch.object(capl_authoring_agent, "_CONFIG_PATH", Path(tmp) / "nonexistent.json"):
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

    def test_call_agent_handles_empty_subprocess_streams(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            completed = SimpleNamespace(returncode=1, stdout=None, stderr=None)
            with patch.dict(os.environ, {capl_authoring_agent.COMMAND_ENV: "fake {payload} {response}"}), patch(
                "workflows.canoe_auto_generation_burr.agents.capl_authoring_agent.subprocess.run",
                return_value=completed,
            ):
                result = capl_authoring_agent.call_agent({"schema_version": "0.1.0"}, root)

        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["stdout"], "")
        self.assertEqual(result["stderr"], "")

    def test_call_agent_uses_configured_outer_timeout(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            completed = SimpleNamespace(returncode=1, stdout=None, stderr=None)
            with patch.dict(os.environ, {
                capl_authoring_agent.COMMAND_ENV: "fake {payload} {response}",
                capl_authoring_agent.TIMEOUT_ENV: "456",
            }), patch(
                "workflows.canoe_auto_generation_burr.agents.capl_authoring_agent.subprocess.run",
                return_value=completed,
            ) as run:
                capl_authoring_agent.call_agent({"schema_version": "0.1.0"}, root)

        self.assertEqual(run.call_args.kwargs["timeout"], 456)

    def test_fixer_payload_uses_only_ir_code_and_latest_error(self) -> None:
        payload = capl_authoring_agent.build_fixer_payload(
            {"cases": [{"case_id": "TC_001"}]},
            "variables\n{\n}\n",
            "latest syntax error",
            3,
        )

        parts = payload["prompt_parts"]
        self.assertEqual([part["name"] for part in parts], [
            "immutable_golden_ir",
            "current_complete_code",
            "latest_compile_error_log",
        ])
        self.assertFalse(parts[0]["replaceable"])
        self.assertTrue(parts[1]["replaceable"])
        self.assertTrue(parts[2]["replaceable"])
        self.assertEqual(parts[2]["content"], "latest syntax error")
        self.assertIn("Generated for CANoe", "\n".join(payload["hard_constraints"]))
        self.assertIn("message MessageType msg_MessageType", "\n".join(payload["hard_constraints"]))

    def test_generate_capl_script_repairs_until_compile_passes(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            agent_script = root / "fake_agent_loop.py"
            compile_script = root / "fake_compile.py"
            agent_script.write_text(
                "\n".join([
                    "import json, sys",
                    "payload = json.load(open(sys.argv[1], encoding='utf-8'))",
                    "role = payload.get('role')",
                    "if role == 'planner':",
                    "    response = {'golden_ir': {'project': payload.get('project'), 'cases': payload.get('cases'), 'capl_api_plan': [], 'assertions': [], 'branching': [], 'evidence_refs': []}}",
                    "else:",
                    "    latest_error = payload['prompt_parts'][2]['content']",
                    "    marker = 'good' if 'syntax error line 7' in latest_error else 'bad'",
                    "    response = {",
                    "      'capl_source': f'/* Generated for CANoe v15 */\\nvariables\\n{{\\n}}\\nvoid MainTest()\\n{{\\n  // {marker}\\n}}\\n',",
                    "      'capl_script_plan': {'assumptions': [], 'adapter_gaps': [], 'used_evidence_refs': [], 'cases': [], 'fix_summary': [marker]}",
                    "    }",
                    "open(sys.argv[2], 'w', encoding='utf-8').write(json.dumps(response))",
                ]),
                encoding="utf-8",
            )
            compile_script.write_text(
                "\n".join([
                    "import json, sys",
                    "capl = open(sys.argv[1], encoding='utf-8').read()",
                    "report = sys.argv[2]",
                    "if '// good' in capl:",
                    "    response = {'status': 'pass', 'message': 'compile ok'}",
                    "else:",
                    "    response = {'status': 'failed', 'message': 'syntax error line 7'}",
                    "open(report, 'w', encoding='utf-8').write(json.dumps(response))",
                    "sys.exit(0 if response['status'] == 'pass' else 1)",
                ]),
                encoding="utf-8",
            )
            state = State({
                "output_root": str(root),
                "structured_test_case": {
                    "project": {"name": "LoopProject", "target_canoe_version": "v15"},
                    "cases": [],
                },
                "project_config": {"strategy": {}},
                "canoe_config_plan": {},
                "cfg_artifact": {"path": str(root / "demo.cfg")},
                "evidence_bundle": {},
                "coverage_report": {},
                "capl_retry_count": 0,
                "capl_compile_max_attempts": 3,
                "canoe_validation_mode": "automated",
            })
            command = f'"{sys.executable}" "{agent_script}" "{{payload}}" "{{response}}"'
            compile_command = f'"{sys.executable}" "{compile_script}" "{{capl}}" "{{report}}"'
            with patch.dict(os.environ, {
                capl_authoring_agent.COMMAND_ENV: command,
                "CANOE_GENE_CAPL_COMPILE_COMMAND": compile_command,
            }):
                result, _ = canoe_workflow.generate_capl_script(state)

            loop = result["capl_script_plan"]["compile_loop"]
            can_text = Path(result["can_artifact"]["path"]).read_text(encoding="utf-8")

        self.assertEqual(loop["status"], "pass")
        self.assertEqual(loop["attempt_count"], 2)
        self.assertIn("// good", can_text)

    def test_generate_capl_script_does_not_fallback_to_builtin_renderer(self) -> None:
        with TemporaryDirectory() as tmp, patch.dict(os.environ, {}, clear=True):
            state = State({
                "output_root": tmp,
                "structured_test_case": {
                    "project": {"name": "AgentOnly", "target_canoe_version": "v15"},
                    "cases": [{"case_id": "TC_001", "name": "demo", "steps": []}],
                },
                "project_config": {"strategy": {"CAPL生成模式": "固定规则"}},
                "canoe_config_plan": {},
                "evidence_bundle": {},
                "coverage_report": {},
                "capl_retry_count": 0,
            })
            self.assertFalse(hasattr(canoe_workflow, "_deterministic_capl_render"))
            result, _ = canoe_workflow.generate_capl_script(state)

            can_path = Path(result["can_artifact"]["path"])
            self.assertEqual(result["capl_script_plan"]["authoring_mode"], "llm_failed")
            self.assertEqual(result["can_artifact"]["renderer"], "llm_kb_indexed_authoring_agent")
            self.assertIn("CAPL LLM authoring failed in strict mode", can_path.read_text(encoding="utf-8"))

    def test_evaluate_capl_script_reuses_compile_loop_result(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            capl = root / "module.can"
            capl.write_text("/* Generated for CANoe v15 */\nvariables\n{\n}\ntestcase TC_001()\n{\n}\n", encoding="utf-8")
            state = State({
                "output_root": str(root),
                "structured_test_case": {
                    "cases": [{"case_id": "TC_001", "steps": [{"step_no": 1}]}],
                },
                "project_config": {},
                "canoe_validation_mode": "automated",
                "cfg_artifact": {},
                "can_artifact": {
                    "path": str(capl),
                    "kind": "capl_test_module_source",
                    "status": "generated",
                    "renderer": "llm_kb_indexed_authoring_agent",
                },
                "capl_script_plan": {
                    "cases": [{"case_id": "TC_001", "steps": [{"step_no": 1}]}],
                    "compile_loop": {
                        "latest_compile_result": {
                            "mode": "automated",
                            "status": "pass",
                            "message": "already compiled",
                            "artifact": str(capl),
                        }
                    },
                },
            })
            with patch("workflows.canoe_auto_generation_burr.vector_canoe_adapter.compile_capl") as compile_capl:
                result, _ = canoe_workflow.evaluate_capl_script(state)

        compile_capl.assert_not_called()
        self.assertEqual(result["capl_eval_status"], "pass")
        self.assertEqual(result["capl_eval_report"]["external_compile"]["message"], "already compiled")


if __name__ == "__main__":
    unittest.main()
