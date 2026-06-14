# coOnBootUp

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coOnBootUp( dword nodeId ); |  |  |  |
| Function | This function is called if a boot-up message was registered on the bus. Each CANopen® node sends this message after the reset during the transition into the state pre-operational. |  |  |  |
| Parameters | nodeId Node-ID, value range 1..127 |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example void coOnBootUp(dword nodeId){ write( "BootUp of node %d recognized", nodeId );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
