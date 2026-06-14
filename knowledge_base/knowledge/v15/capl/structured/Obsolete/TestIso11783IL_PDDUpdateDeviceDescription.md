# TestIso11783IL_PDDUpdateDeviceDescription

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: Iso11783IL_PDDUpdateDeviceDescription |  |  |  |  |
|---|---|---|---|---|
| Note The ISO11783 Interaction Layer allows the segmented transmission of device descriptions. |  |  |  |  |
| Function Syntax | long TestIso11783IL_PDDUpdateDeviceDescription( dbNode node, char deviceCfgPath [] ); |  |  |  |
| Function | The function updates the current device description object pool at run-time. Only the device object and objects of type DeviceValuePresentation of the specified file are transmitted. Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. | Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |
| Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |
| Parameters | node Simulation node to apply the function. |  |  |  |
| deviceCfgPath file name of the device configuration file The file must be located in the directory of the CANoe configuration. |  |  |  |  |
| Return Values | error code |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.5 | ISO11783 Test nodes | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
