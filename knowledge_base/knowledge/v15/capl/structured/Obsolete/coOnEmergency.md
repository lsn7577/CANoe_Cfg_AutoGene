# coOnEmergency

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coOnEmergency( dword nodeId, dword errorCode, dword errorRegister ); |  |  |  |
| Function | This function is called if an emergency message was received. Data of manufacturer emergency codes can be read with coThisGetData. |  |  |  |
| Parameters | nodeId Node-ID, value range 1..127 |  |  |  |
| errorCode Emergency error code, value range 0..65.535 |  |  |  |  |
| errorRegister Content of the error register |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example void coOnEmergency( dword nodeId, dword errorCode, dword errorRegister ){ write( "Emergency message from node %d with error code 0x%X received", nodeId, errorCode );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
