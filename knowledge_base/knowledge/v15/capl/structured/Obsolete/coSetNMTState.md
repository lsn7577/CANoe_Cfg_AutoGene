# coSetNMTState

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coSetNMTState( dword nodeId, dword newState,dword errCode[] ); |  |  |  |
| Function | Sets the state of a node on the network. The node for which this function is called must previously have been started with coStartUp(). Furthermore, the node must be configured as NMT master (Bit 0 in 1F80 set) and the object 1F82 must exist in the object dictionary. |  |  |  |
| Parameters | nodeId Node-ID, value range 0..127, 0 - all nodes |  |  |  |
| newState Desired state of the node4 - stopped5 - operational6 - reset node7 - reset communication127 - pre-operational |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coSetNMTState( 0, 5, errCode );if (errCode[0] == 0) { write( "NMT state change to Operational for all nodes commanded" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
