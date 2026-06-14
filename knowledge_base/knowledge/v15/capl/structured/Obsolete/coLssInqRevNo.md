# coLssInqRevNo

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coLssInqRevNo( dword errCode[] ); |  |  |  |
| Function | This service causes the determination of the revision number of a LSS slave. It is available in configuration mode only and there may only be one LSS slave in this mode. |  |  |  |
| Parameters | errCode Error code buffer (is entered in index 0 of the field) |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coLssInqRevNo( errCode );if (errCode[0] == 0) { write( "LSS inquire Revision-Number commanded" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
