# MCDStatusIndication

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Merely due to compatibility reasons ASAM MCD3 via CANape is currently still available.Please use CANoe option .AMD/XCP instead. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | MCDStatusIndication( char moduleName[], long operation, long status) |  |  |  |
| Function | Callback handler for different MCD status. The function provides the status of successful/ not successful data acquisition starts. |  |  |  |
| Parameters | modulName Module name configured in the global option dialog. External Programs\|MCD 3D Server. |  |  |  |
| operation Operation ID, which shows the status. 1 – Start Data Acq |  |  |  |  |
| Status 1: Successful0: Fail |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP4 | ASAM-MCD | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
