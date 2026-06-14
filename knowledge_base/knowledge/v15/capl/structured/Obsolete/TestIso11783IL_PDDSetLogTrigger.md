# TestIso11783IL_PDDSetLogTrigger

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: Iso11783IL_PDDSetLogTrigger |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Function Syntax | long TestIso11783IL_PDDSetLogTrigger( dbNode node, dword command, ulong ddi, ulong elNum, ulong value ); |  |  |  |  |  |  |  |
| Function | A measurement command can be executed with this function. It can be used in the callback function Iso11783IL_PDDOnDefaultLogRequest to activate the default logging. Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. | Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |  |  |
| Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |  |  |  |  |
| Parameters | node Simulation node to apply the function. |  |  |  |  |  |  |  |
| command measurement command: 4: Time Interval 5: Distance Interval 6: Minimum within Threshold 7: Maximum within Threshold 8: Change Threshold |  |  |  |  |  |  |  |  |
| ddi Data Dictionary Identifier, 0x0000..0xFFFF |  |  |  |  |  |  |  |  |
| elNum element number, 0x000..0xFFF |  |  |  |  |  |  |  |  |
| value depends on command Command Value Time Interval time in ms Distance Interval distance in mm Minimum within ThresholdMaximum within ThresholdChange Threshold value of the process variable use value 0 to disable a trigger | Command | Value | Time Interval | time in ms | Distance Interval | distance in mm | Minimum within ThresholdMaximum within ThresholdChange Threshold | value of the process variable |
| Command | Value |  |  |  |  |  |  |  |
| Time Interval | time in ms |  |  |  |  |  |  |  |
| Distance Interval | distance in mm |  |  |  |  |  |  |  |
| Minimum within ThresholdMaximum within ThresholdChange Threshold | value of the process variable |  |  |  |  |  |  |  |
| Return Values | 0: function has been executed successfully <0: an error has occurred |  |  |  |  |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |  |  |
| 8.5 | ISO11783 Test nodes | — | • |  |  |  |  |  |
| Example — |  |  |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
