from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

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


if __name__ == "__main__":
    unittest.main()
