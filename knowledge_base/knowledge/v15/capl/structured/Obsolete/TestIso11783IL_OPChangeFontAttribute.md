# TestIso11783IL_OPChangeFontAttribute

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: Iso11783IL_OPChangeFontAttribute |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long TestIso11783IL_OPChangeFontAttribute( dbNode node, dword objectID, dword color, dword size, dword type, dword style ); |  |  |  |
| Function | The function changes the properties of a font attribute object. A Change Font Attribute command is sent to the Virtual Terminal. Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. | Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |
| Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |
| Parameters | node Simulation node to apply the function. |  |  |  |
| objectID Object ID of the font attribute object |  |  |  |  |
| color Color index |  |  |  |  |
| size Size of the font: 0: 6x8 1: 8x8 2: 8x12 3: 12x16 4: 16x16 5: 16x24 6: 24x32 7: 32x32 8: 32x48 9: 48x64 10: 64x64 11: 64x96 12: 96x128 13: 128x128 14: 128x192 |  |  |  |  |
| type Font type: 0: ISO8859-1 (ISO Latin 1) 1: ISO8859-15 (ISO Latin 9) 2: ISO8859-2 (ISO Latin 2) |  |  |  |  |
| style Font style: Bit 0: 1 Bold Bit 1: 1 Crossed out Bit 2: 1 Underlined Bit 3: 1 Italic Bit 4: 1 Inverted Bit 5: 1 Flashing |  |  |  |  |
| Return Values | 0: Function has been executed successfully |  |  |  |
| <0: An error has occurred, see error codes |  |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.5 | ISO11783 Test nodes | — | • |  |
| Example testcase StructuredDataSample(){ long table = 0; TestCaseDescription("Shows how to display a user-defined info table."); TestStepPass(0, "1", "First Step"); // begin table table = TestInfoTable("User Structured Data"); // header TestInfoHeadingBegin(table, 0); TestInfoCell(table, "Left part"); TestInfoCell(table, "Operation"); TestInfoCell(table, "Right part"); TestInfoCell(table, "Result"); TestInfoHeadingEnd(table); // row 1 TestInfoRow(table, 0); TestInfoCell(table, "Frequency"); TestInfoCell(table, "<"); TestInfoCell(table, "50"); TestInfoCell(table, "warning"); // row 2 TestInfoRow(table, 0); TestInfoCell(table, "Temperature"); TestInfoCell(table, "in range"); TestInfoCell(table, "90-100"); TestInfoCell(table, "pass"); // intermediate header TestInfoHeadingBegin(table, 1); TestInfoCell(table, "Additional conditions", 4); TestInfoHeadingEnd(table); // row 4 TestInfoRow(table, 1); TestInfoCell(table, "Test Duration", 2); TestInfoCell(table, "60s"); TestInfoCell(table, "fail"); // output table TestStepFail(0, "2", table);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
