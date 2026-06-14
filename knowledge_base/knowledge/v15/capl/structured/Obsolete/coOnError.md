# coOnError

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coOnError( dword errorCode, dword errorClass, dword nodeId, dword index, dword subIndex, dword param ); |  |  |  |
| Function | This function is called if an error occurs. |  |  |  |
| Parameters | errorCode Error code (see error codes of coOnError) |  |  |  |
| errorClass Error class |  |  |  |  |
| nodeId Node-ID, value range 1..127 |  |  |  |  |
| index Index of the object, value range 1..65.535 |  |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| param Additional error parameter (see error codes of coOnError) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example void coOnError( dword errorCode, dword errorClass, dword nodeId, dword index, dword subIndex, dword param){ write( "Error occurred, code = 0x%X, class = %d", errorCode, errorClass );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
