# TestIso11783IL_OPSelectInput

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: Iso11783IL_OPSelectInput |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long TestIso11783IL_OPSelectInput( dbNode node, dword objectID, dword select ); |  |  |  |
| Function | The function selects an input object. A Select Input command is sent to the Virtual Terminal. Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. | Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |
| Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |
| Parameters | node Simulation node to apply the function. |  |  |  |
| objectID object ID of an input object |  |  |  |  |
| select 0: no input object shall be selected (i.e. focus is removed) 1: select input object 2: open input object for user input (only version >= 3) |  |  |  |  |
| Return Values | 0: function has been executed successfully <0: an error has occurred, see error codes |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.5 | ISO11783 Test nodes | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
