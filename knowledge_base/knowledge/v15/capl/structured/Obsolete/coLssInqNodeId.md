# coLssInqNodeId

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coLssInqNodeId( dword errCode[] ); |  |  |  |
| Function | This service causes the determination of the node-ID of a LSS slave. It is available in configuration mode only and there may only be one LSS slave in this mode. |  |  |  |
| Parameters | errCode Error code buffer (is entered in index 0 of the field) |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coLssInqNodeId( errCode );if (errCode[0] == 0) { write( "LSS inquire node-ID commanded" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
