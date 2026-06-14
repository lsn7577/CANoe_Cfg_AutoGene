# MCDParamResponse

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Merely due to compatibility reasons ASAM MCD3 via CANape is currently still available.Please use CANoe option .AMD/XCP instead. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long MCDParamResponse ( char moduleName[], char parameterName[], double value) |  |  |  |
| Function | Callback handler on a MCDGetECUParam request. This function must be defined in the CAPL program to get a response on a read request. |  |  |  |
| Parameters | moduleName Name of the module that is configured in the global options dialog External Programs\|MCD 3D Server. |  |  |  |
| parameterName Name of the parameter. |  |  |  |  |
| value Value of the parameter. |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP4 | ASAM-MCD | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
