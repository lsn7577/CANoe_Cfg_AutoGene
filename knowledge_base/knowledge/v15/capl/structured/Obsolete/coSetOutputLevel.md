# coSetOutputLevel

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coSetOutputLevel( dword level, dword errCode[] ); |  |  |  |
| Function | The function sets the output level of the node layer. Note It must be noted that this function may only be called if the node has been started. | Note It must be noted that this function may only be called if the node has been started. |  |  |
| Note It must be noted that this function may only be called if the node has been started. |  |  |  |  |
| Parameters | level Output level, value range 0..10 |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coSetOutputLevel( 5, errCode ); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
