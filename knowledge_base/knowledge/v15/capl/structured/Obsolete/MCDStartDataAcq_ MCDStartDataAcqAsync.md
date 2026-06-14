# MCDStartDataAcq/ MCDStartDataAcqAsync

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Merely due to compatibility reasons ASAM MCD3 via CANape is currently still available.Please use CANoe option .AMD/XCP instead. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long MCDStartDataAcq( char moduleName[], int taskId, int pollingRate, char parameters[]) |  |  |  |
| long MCDStartDataAcqAsync( char moduleName[], int taskId, int pollingRate, char parameters[]) |  |  |  |  |
| Function | Configure and start the data acquisition. After a data acquisition is started the configured parameters are transferred to CANoe with the specified polling rate. The values can be obtained with MCDGetCurrentValue. Using MCDStartDataAcqAsync the data acquisition is started asynchronous. This means that the current measuring is not interrupted during the call of this function. |  |  |  |
| Parameters | ModuleName Name of the module that is configured in the global options dialog External Programs\|MCD 3D Server. |  |  |  |
| taskId Id of the task which is available. |  |  |  |  |
| pollingRate Cycle time with which the values are reported to CANoe internally. |  |  |  |  |
| parameters A string that specifies the parameters which are cyclically reported to CANoe. The parameters are separated with ';'. Note: the size of the string must contain the null terminator. Example for a string that specifies a0, b0 and c0 as parameters: char paramStr[9] = "a0;b0;c0"; |  |  |  |  |
| Return Values | 0 |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP4 | ASAM-MCD | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
