# coGetNodeId

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword coGetNodeId( dword errCode[] ); |  |  |  |
| Function | The function returns the node-ID. If the function coStartUp was not executed yet, the function returns 0. |  |  |  |
| Parameters | errCode Error code buffer (is entered in index 0 of the field) |  |  |  |
| Return Values | Node-ID |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];dword nodeId;nodeId = coGetNodeId( errCode ); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
