# TestIso11783IL_PDDSetDistance

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: Iso11783IL_PDDSetDistance |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long TestIso11783IL_PDDSetDistance( dbNode node, dword distance ); |  |  |  |
| Function | The distance covered is set with this function. The value is needed for the distance trigger and should be updated cyclically. Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. | Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |
| Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |
| Parameters | node Simulation node to apply the function. |  |  |  |
| distance distance covered in [m] |  |  |  |  |
| Return Values | 0: function has been executed successfully <0: an error has occurred |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.5 | ISO11783 Test nodes | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
