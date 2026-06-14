# coOnLssEvent

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coOnLssEvent( dword evType, dword param, dword param2 ); |  |  |  |
| Function | This function is called if the response of a LSS command was received. This can be triggered by one of the LSS functions. If during the execution an error occurs, the event function coOnError is called instead of these. |  |  |  |
| Parameters | evType LSS event type |  |  |  |
| param Additional parameter - dependent on evType (see LSS event types) |  |  |  |  |
| param2 Additional parameter - dependent on evType (see LSS event types) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example void coOnLssEvent( dword evType, dword param, dword param2 ){ write( "LSS event occurred 0x%x", evType );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
