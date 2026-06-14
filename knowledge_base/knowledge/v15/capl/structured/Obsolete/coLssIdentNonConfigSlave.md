# coLssIdentNonConfigSlave

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coLssIdentNonConfigSlave( dword errCode[] ); |  |  |  |
| Function | With this service, the LSS master commands all LSS slaves whose node-ID is not configured (0xFF) to identify themselves. |  |  |  |
| Parameters | errCode Error code buffer (is entered in index 0 of the field) |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coLssIdentNonConfigSlave( errCode );if (errCode[0] == 0) { write( "LSS identify non-configured slaves commanded" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
