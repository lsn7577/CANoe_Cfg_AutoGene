# TestIso11783IL_OPSaveAuxAssignment

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: Iso11783IL_OPSaveAuxAssignment |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long TestIso11783IL_OPSaveAuxAssignment( dbNode node, char filename[] ); |  |  |  |
| Function | The function saves the current auxiliary input assignment as Preferred Auxiliary Input Assignment in an INI file. With the function Iso11783IL_OPLoadAuxAssignment the "Preferred Assignment" can be load and used again. Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. | Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |
| Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |
| Parameters | node Simulation node to apply the function. |  |  |  |
| filename File name of an ini file (*.INI) |  |  |  |  |
| Return Values | 0: Function has been executed successfully |  |  |  |
| <0: An error has occurred, see error codes |  |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.5 | ISO11783 Test nodes | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
