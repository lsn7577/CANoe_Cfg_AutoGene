# MCDMapECUParamToSysVariableWrite

> Category: `Obsolete` | Type: `notes`

## Description

MCDMapECUParamToSysVariableRead | MCDSetECUParam

| Deprecated Function Merely due to compatibility reasons ASAM MCD3 via CANape is currently still available.Please use CANoe option .AMD/XCP instead. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long MCDMapECUParamToSysVariableWrite(char moduleName[], char parameterName[], SysVarName) |  |  |  |
| Function | Maps an ECU parameter to a system variable so that it is changed whenever the system variable changes. |  |  |  |
| Parameters | moduleName Name of the module that is configured in the global options dialog External Programs\|MCD 3D Server. |  |  |  |
| parameterName Name of the parameter. |  |  |  |  |
| SysVarName System variable. |  |  |  |  |
| Return Values | 0: No error. |  |  |  |
| 1: The parameter is already mapped as write target of another system variable. |  |  |  |  |
| 2: The parameter is already mapped as write target of this system variable. |  |  |  |  |
| 3: The system variable is already mapped as write source of a different parameter. |  |  |  |  |
| 4: The system variable is already mapped as read target of a different parameter. |  |  |  |  |
| 5: The system variable is not of type float. |  |  |  |  |
| -1: An internal error occurred. |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP4 | ASAM-MCD | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
