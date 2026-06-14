# TestIso11783IL_OPGetVersion

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: Iso11783IL_OPGetVersion |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long TestIso11783IL_OPGetVersion( dbNode node ); |  |  |  |
| long TestIso11783IL_OPGetVersion( dbNode node, byte extendedVersions ); |  |  |  |  |
| Function | The function requests the stored object pools from the Virtual Terminal. A Get Version command or a Get Extended Version command is sent to the Virtual Terminal. If a response from the Virtual Terminal is received, the callback function Iso11783IL_OPOnResponse is called. Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. | Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |
| Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |
| Parameters | node Simulation node to apply the function. |  |  |  |
| extendedVersions kind of versions to query. To get extended versions a VT version 5 or higher is necessary. 0: get standard version strings (7 characters) 1: get extended version strings (32 characters) |  |  |  |  |
| Return Values | 0: function has been executed successfully <0: an error has occurred, see error codes |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.5 | ISO11783 Test nodes | — | • |  |
| Example testcase StructuredDataSample(){ long table = 0; TestCaseDescription("Shows how to display a user-defined info table."); TestStepPass(0, "1", "First Step"); // begin table table = TestInfoTable("User Structured Data"); // header TestInfoHeadingBegin(table, 0); TestInfoCell(table, "Left part"); TestInfoCell(table, "Operation"); TestInfoCell(table, "Right part"); TestInfoCell(table, "Result"); TestInfoHeadingEnd(table); // row 1 TestInfoRow(table, 0); TestInfoCell(table, "Frequency"); TestInfoCell(table, "<"); TestInfoCell(table, "50"); TestInfoCell(table, "warning"); // row 2 TestInfoRow(table, 0); TestInfoCell(table, "Temperature"); TestInfoCell(table, "in range"); TestInfoCell(table, "90-100"); TestInfoCell(table, "pass"); // intermediate header TestInfoHeadingBegin(table, 1); TestInfoCell(table, "Additional conditions", 4); TestInfoHeadingEnd(table); // row 4 TestInfoRow(table, 1); TestInfoCell(table, "Test Duration", 2); TestInfoCell(table, "60s"); TestInfoCell(table, "fail"); // output table TestStepFail(0, "2", table);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
