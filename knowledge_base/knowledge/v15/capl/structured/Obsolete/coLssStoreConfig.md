# coLssStoreConfig

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coLssStoreConfig( dword errCode[] ); |  |  |  |
| Function | The configured parameters are written into non-volatile memory with this service. Only one LSS slave may be in configuration mode. |  |  |  |
| Parameters | errCode Error code buffer (is entered in index 0 of the field) |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coLssStoreConfig( errCode );if (errCode[0] == 0) { write( "LSS store configuration commanded" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
