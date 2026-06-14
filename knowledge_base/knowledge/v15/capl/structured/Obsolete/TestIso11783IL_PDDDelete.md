# TestIso11783IL_PDDDelete

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: Iso11783IL_PDDDelete |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long TestIso11783IL_PDDDelete( dbNode node ); |  |  |  |
| Function | Deletes the process data directory and disconnects from the Task Controller. Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. | Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |
| Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |
| Parameters | node Simulation node to apply the function. |  |  |  |
| Return Values | 0: process data directory has been deleted successfully <0: an error has occurred |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.5 | ISO11783 Test nodes | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
