# MCDGetECUParam

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Merely due to compatibility reasons ASAM MCD3 via CANape is currently still available.Please use CANoe option .AMD/XCP instead. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long MCDGetECUParam ( char moduleName[], char parameterName[], int format) |  |  |  |
| Function | Reading of a parameter. The read parameter value will be available in the MCDParamResponse callback handler. |  |  |  |
| Parameters | ModuleName Name of the module that is configured in the global options dialog External Programs\|MCD 3D Server. |  |  |  |
| parameterName Name of the parameter to be read. |  |  |  |  |
| format Read out format: 0 – hex, ECU intern1 – physical representation |  |  |  |  |
| Return Values | 0: OK |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP4 | ASAM-MCD | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
