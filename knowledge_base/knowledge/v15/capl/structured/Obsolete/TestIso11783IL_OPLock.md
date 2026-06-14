# TestIso11783IL_OPLock

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: Iso11783IL_OPLock |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long TestIso11783IL_OPLock( dbNode node, dword lock, dword maskID, dword timeout ); |  |  |  |
| Function | The function locks the screen updates on the Virtual Terminal. A Lock command is sent to the Virtual Terminal. Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. | Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |
| Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |
| Parameters | node Simulation node to apply the function. |  |  |  |
| lock 0: unlock 1: lock |  |  |  |  |
| maskID object ID of the data mask object |  |  |  |  |
| timeout timeout in [ms] |  |  |  |  |
| Return Values | 0: function has been executed successfully <0: an error has occurred, see error codes |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.5 | ISO11783 Test nodes | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
