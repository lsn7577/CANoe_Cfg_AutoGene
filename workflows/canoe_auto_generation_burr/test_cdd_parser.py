from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from workflows.canoe_auto_generation_burr.canoe_workflow import _cdd_contains, _parse_cdd_file


class CddParserTest(unittest.TestCase):
    def test_protocol_service_and_did_aliases_are_matchable(self) -> None:
        sample = """<?xml version='1.0' encoding='utf-8'?>
<CANDELA>
<DIDS>
<DID id='did1' n='61840'>
<NAME><TUV xml:lang='en-US'>VINDataIdentifier</TUV></NAME>
<QUAL>VIN</QUAL>
<STRUCTURE>
<DATAOBJ dtref='ascii17'><NAME><TUV xml:lang='en-US'>VIN</TUV></NAME><QUAL>VIN</QUAL></DATAOBJ>
</STRUCTURE>
</DID>
</DIDS>
<PROTOCOLSERVICES>
<PROTOCOLSERVICE id='svc10' func='1' phys='1' respOnPhys='1' respOnFunc='1'>
<NAME><TUV xml:lang='en-US'>($10) DiagnosticSessionControl</TUV></NAME>
<QUAL>DSC</QUAL>
<REQ><CONSTCOMP spec='sid' v='16'/></REQ>
<POS><CONSTCOMP spec='sid' v='80'/></POS>
</PROTOCOLSERVICE>
</PROTOCOLSERVICES>
</CANDELA>
"""
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.cdd"
            path.write_text(sample, encoding="utf-8")
            model = _parse_cdd_file(path)

        source_models = {"cdd": {"files": [{"status": "parsed", "model": model}]}}
        self.assertTrue(_cdd_contains(source_models, "DiagnosticSessionControl"))
        self.assertTrue(_cdd_contains(source_models, "DSC"))
        self.assertTrue(_cdd_contains(source_models, "0x10"))
        self.assertTrue(_cdd_contains(source_models, "F190"))
        self.assertTrue(_cdd_contains(source_models, "VINDataIdentifier"))


if __name__ == "__main__":
    unittest.main()
