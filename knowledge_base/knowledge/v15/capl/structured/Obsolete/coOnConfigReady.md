# coOnConfigReady

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coOnConfigReady( dword event, dword nodeId ); |  |  |  |
| Function | During the start, a simulated node as configuration manager can supply other nodes on the network with configuration data. This data is then transmitted via SDO by the simulated configuration manager. The function informs the user about the current state of the configuration process. |  |  |  |
| Parameters | event Event type |  |  |  |
| nodeId Node-ID, value range 0..127 |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example void coOnConfigReady( dword event, dword nodeId ){ dword errCode[1]; switch (event) { case 0: write( "Configuration management started" ); break; case 1: write( "Wait for start" ); break; case 2: write( "All mandatory nodes configured" ); break; case 3: if (nodeId) { write( "Node %d configured", nodeId ); } else { write( "All nodes configured" ); } break; case 4: write( "Software update state reached" ); coAllowStart(errCode); // go on with boot process by default break; case 5: write( "Output level set differing from default" ); break; case 6: write( "Mandatory node fails error control - NMT reset all nodes transmitted" ); break; case 7: write( "Mandatory node fails error control - NMT stop all nodes transmitted" ); break; };} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
