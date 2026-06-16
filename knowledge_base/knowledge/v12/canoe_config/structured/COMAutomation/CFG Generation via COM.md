# CFG Generation via COM

CANoe 12 exposes a COM Automation object model for configuration creation and saving. The supported path is to start CANoe.Application, create or open a configuration, modify supported setup objects, and call Configuration.SaveAs so CANoe writes the .cfg.

No stable public .cfg writing grammar was found in Help01; treat .cfg text as proprietary CANoe state.

Use this page only for CANoe configuration workflow retrieval. CAPL writing should use the capl_authoring profile instead.