# SCC_ShutdownInstant

> Category: `SmartCharging` | Type: `notes`

| Deprecated Function This function is deprecated. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long SCC_Shutdown ( long Terminate ) |  |  |  |
| Function | Stops the charging session when inside the charge loop, by starting a regular shutdown procedure. |  |  |  |
| Parameters | Terminate If 1, the SessionStopReq is sent with ChargingSession = Terminate, else with ChargingSession = Pause (ISO 15118 only, else this value is ignored). |  |  |  |
| Return Values | 0: Not successful |  |  |  |
| 1: Successful |  |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 11.0 SP3 | Ethernet .SmartCharging | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
