# TestIso11783IL_PDDLoadDeviceDescription

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: Iso11783IL_PDDLoadDeviceDescription |  |  |  |  |
|---|---|---|---|---|
| Note In case the corresponding node is running in the distributed environment, the machine configuration file has to be registered under Configuration\|Options…\|Configuration Settings\|User files in CANoe. The ISO11783 Interaction Layer allows the segmented transmission of device descriptions. |  |  |  |  |
| Function Syntax | long TestIso11783IL_PDDLoadDeviceDescription( dbNode node, char deviceCfgPath[] ); |  |  |  |
| Function | The function creates a process data dictionary from a machine configuration file (XML). Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. | Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |
| Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |
| Parameters | node Simulation node to apply the function. |  |  |  |
| deviceCfgPath file name of the machine configuration file The file must be located in the directory of the CANoe configuration. |  |  |  |  |
| Return Values | 0: process data dictionary has been created successfully <0: an error has occurred |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.5 | ISO11783 Test nodes | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
