import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import subprocess
import unittest
from unittest.mock import patch

from workflows.canoe_auto_generation_burr import vector_canoe_adapter


class VectorCanoeAdapterTest(unittest.TestCase):
    def test_cfg_automation_script_uses_official_com_surface(self) -> None:
        plan = {
            "target_canoe_version": "v12",
            "base_cfg_template": r"C:\demo\base.cfg",
            "channels": [{"CANoe通道名": "CAN"}],
            "mounted_files": {
                "dbc": [r"C:\demo\network.dbc"],
                "cdd": [r"C:\demo\diag.cdd"],
                "a2l": [r"C:\demo\ecu.a2l"],
                "dll": [r"C:\demo\seedkey.dll"],
            },
            "test_modules": [{"source": r"C:\demo\module.can"}],
        }
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            plan_path = root / "cfg.plan.json"
            output_cfg = root / "out.cfg"
            script_path = root / "generate.ps1"
            plan_path.write_text("{}", encoding="utf-8")

            result = vector_canoe_adapter.write_cfg_automation_script(plan, plan_path, output_cfg, script_path)
            script = script_path.read_text(encoding="utf-8")

        self.assertEqual(result["status"], "script_written")
        self.assertIn("New-Object -ComObject CANoe.Application", script)
        self.assertIn(".DatabaseSetup.Databases.Add", script)
        self.assertIn(".DiagnosticsSetup.DiagDescriptions.Add", script)
        self.assertIn(".XCPSetup.ECUs.Add", script)
        self.assertIn(".CLibraries.Add", script)
        self.assertIn(".SaveAs(", script)

    def test_compile_capl_uses_configured_compile_command(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            capl = root / "module.can"
            capl.write_text("/* Generated for CANoe v15 */\nvariables\n{\n}\n", encoding="utf-8")
            script = root / "compile.py"
            script.write_text(
                "\n".join([
                    "import json, sys",
                    "open(sys.argv[2], 'w', encoding='utf-8').write(json.dumps({'status': 'pass', 'message': 'ok'}))",
                ]),
                encoding="utf-8",
            )
            command = f'"{sys.executable}" "{script}" "{{capl}}" "{{report}}"'
            with patch.dict(os.environ, {vector_canoe_adapter.CAPL_COMPILE_COMMAND_ENV: command}):
                result = vector_canoe_adapter.compile_capl(
                    {"path": str(capl)},
                    mode="automated",
                    output_root=root,
                    attempt=2,
                )

        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["message"], "ok")
        self.assertTrue(result["report_file"].endswith("capl_compile_attempt_2.json"))

    def test_capl_compile_script_uses_canoe_capl_com_surface(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            capl = root / "module.can"
            cfg = root / "project.cfg"
            report = root / "compile.json"
            script_path = root / "compile.ps1"
            capl.write_text("/* Generated for CANoe v15 */", encoding="utf-8")
            cfg.write_text("", encoding="utf-8")

            result = vector_canoe_adapter.write_capl_compile_script(capl, report, script_path, cfg)
            script = script_path.read_text(encoding="utf-8")

        self.assertEqual(result["status"], "script_written")
        self.assertIn("Configuration.RunCompilation", script)
        self.assertIn("Configuration.Compile", script)
        self.assertIn("InvokeMember($MethodName, 'InvokeMethod'", script)
        self.assertIn("CAPL.Compile", script)
        self.assertIn("GetCompilationResult", script)
        self.assertIn("$Application.CAPL.CompileResult", script)
        self.assertIn("ErrorMessage", script)
        self.assertIn("NodeName", script)
        self.assertIn("SourceFile", script)
        self.assertIn("Open-CanoeConfiguration", script)
        self.assertIn("creating a fresh configuration before compilation", script)
        self.assertIn("warnings = $warnings", script)

    def test_compile_capl_generates_builtin_com_script_when_no_hook(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            capl = root / "module.can"
            capl.write_text("/* Generated for CANoe v15 */\nvariables\n{\n}\n", encoding="utf-8")
            with patch.dict(os.environ, {}, clear=True), patch.object(
                vector_canoe_adapter,
                "is_available",
                return_value={"available": False, "reason": "not installed"},
            ):
                result = vector_canoe_adapter.compile_capl(
                    {"path": str(capl)},
                    mode="automated",
                    output_root=root,
                    attempt=3,
                )
            script = Path(result["script"]).read_text(encoding="utf-8")

        self.assertEqual(result["status"], "unavailable")
        self.assertIn("capl_compile_attempt_3.ps1", result["script"])
        self.assertIn("CAPL.Compile", script)
        self.assertNotIn("no project-specific compile hook", result["message"])

    def test_prepare_cfg_generation_handles_empty_subprocess_streams(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            plan_path = root / "cfg.plan.json"
            output_cfg = root / "out.cfg"
            script_path = root / "generate.ps1"
            plan_path.write_text("{}", encoding="utf-8")

            completed = SimpleNamespace(returncode=1, stdout=None, stderr=None)
            with patch.object(vector_canoe_adapter, "is_available", return_value={"available": True, "reason": "ok"}), patch(
                "workflows.canoe_auto_generation_burr.vector_canoe_adapter.subprocess.run",
                return_value=completed,
            ):
                result = vector_canoe_adapter.prepare_cfg_generation({}, plan_path, output_cfg, script_path, mode="automated")

        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["stdout"], "")
        self.assertEqual(result["stderr"], "")

    def test_compile_capl_handles_empty_subprocess_streams(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            capl = root / "module.can"
            capl.write_text("/* Generated for CANoe v15 */", encoding="utf-8")

            completed = SimpleNamespace(returncode=1, stdout=None, stderr=None)
            with patch.dict(os.environ, {vector_canoe_adapter.CAPL_COMPILE_COMMAND_ENV: "compile {capl} {report}"}), patch(
                "workflows.canoe_auto_generation_burr.vector_canoe_adapter.subprocess.run",
                return_value=completed,
            ):
                result = vector_canoe_adapter.compile_capl({"path": str(capl)}, mode="automated", output_root=root, attempt=1)

        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["stdout"], "")
        self.assertEqual(result["stderr"], "")

    def test_compile_capl_returns_structured_timeout_failure(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            capl = root / "module.can"
            capl.write_text("/* Generated for CANoe v15 */", encoding="utf-8")

            with patch.dict(os.environ, {vector_canoe_adapter.CAPL_COMPILE_COMMAND_ENV: "compile {capl} {report}", vector_canoe_adapter.CAPL_COMPILE_TIMEOUT_ENV: "1"}), patch(
                "workflows.canoe_auto_generation_burr.vector_canoe_adapter.subprocess.run",
                side_effect=subprocess.TimeoutExpired(cmd="compile", timeout=1, output="out", stderr="err"),
            ):
                result = vector_canoe_adapter.compile_capl({"path": str(capl)}, mode="automated", output_root=root, attempt=1)

        self.assertEqual(result["status"], "failed")
        self.assertIn("timed out", result["message"])
        self.assertEqual(result["details"]["timeout_seconds"], 1)


if __name__ == "__main__":
    unittest.main()
