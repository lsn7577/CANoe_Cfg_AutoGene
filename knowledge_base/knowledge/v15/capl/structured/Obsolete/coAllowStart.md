# coAllowStart

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coAllowStart( dword errCode[] ); |  |  |  |
| Function | If a simulated node is configured as NMT master (Bit 0 in 1F80 set), there are various states during the start procedure in which the application is signaled by the event function coOnConfigReady. In these states, the simulated node waits for the release of the application in order to be able to continue the start procedure. The various events and the associated information can be read in the description of coOnConfigReady. |  |  |  |
| Parameters | errCode Error code buffer (is entered in index 0 of the field) |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example void coOnConfigReady ( dword event, dword nodeId ){ dword errCode[1]; switch (event) { case 1: write( "Wait for start" ); coAllowStart ( errCode ); // switch to operational break; case 4: write( "Software update state reached" ); coAllowStart( errCode ); // go on with boot process by default break; };} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
