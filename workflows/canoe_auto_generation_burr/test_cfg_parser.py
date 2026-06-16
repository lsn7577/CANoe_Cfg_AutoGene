from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from workflows.canoe_auto_generation_burr.canoe_workflow import _parse_cfg_file
from workflows.canoe_auto_generation_burr.canoe_workflow import _source_files_from_state


class CfgParserTest(unittest.TestCase):
    def test_cfg_file_references_are_grouped_by_extension(self) -> None:
        sample = ''';CANoe Version |4|12|2|52400 EQ07
Version: 12.0.75 Build 75
<VFileName V8 QL> 1 "example.dbc"
<VFileName V8 BQL> 1 base=cfg "diag.cdd"
<a2l><VFileName v="V8" f="QL" init="1" name="model.a2l" /></a2l>
'''
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "EQ07.cfg"
            path.write_text(sample, encoding="utf-8")
            model = _parse_cfg_file(path)

        self.assertEqual(model["version"], "12.0.75 Build 75")
        self.assertIn("example.dbc", model["mounted_files"]["dbc"])
        self.assertIn("diag.cdd", model["mounted_files"]["cdd"])
        self.assertIn("model.a2l", model["mounted_files"]["a2l"])

    def test_dll_is_discovered_next_to_declared_sources(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            dbc = root / "network.dbc"
            dll = root / "XcpSeedNKey.dll"
            dbc.write_text("VERSION \"demo\"", encoding="utf-8")
            dll.write_bytes(b"MZ")
            project_config = {
                "basic": {},
                "enabled_channels": [{"DBC路径": str(dbc), "启用": "是"}],
                "strategy": {},
            }

            sources = _source_files_from_state({}, project_config)

        self.assertEqual(sources["dll"], [str(dll)])


if __name__ == "__main__":
    unittest.main()
