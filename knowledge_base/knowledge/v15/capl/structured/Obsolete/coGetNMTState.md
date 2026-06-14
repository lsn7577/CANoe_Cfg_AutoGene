# coGetNMTState

> Category: `Obsolete` | Type: `notes`

## Description

Current communication state of the node

0 - unknown or failed4 - stopped5 - operational127 - pre-operational

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword coGetNMTState( dword nodeId, dword errCode[] ); |  |  |  |
| Function | Returns the state of a node on the network. The node for which this function is called must previously have been started with coStartUp. Furthermore, the node must be configured as NMT master (Bit 0 in 1F80 set) and the object 1F82 must exist in the object dictionary. Note The NMT state of a node can only be determined if it is monitored. | Note The NMT state of a node can only be determined if it is monitored. |  |  |
| Note The NMT state of a node can only be determined if it is monitored. |  |  |  |  |
| Parameters | nodeId node-ID, value range 1..127 |  |  |  |
| errCode Error code buffer (error code is entered in index 0 of this array) |  |  |  |  |
| Return Values | Current communication state of the node 0 - unknown or failed4 - stopped5 - operational127 - pre-operational |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];dword nmtState;nmtState = coGetNMTState( 10, errCode );if (errCode[0] == 0){ write( "NMT state successfully requested" );}if (nmtState == 5){ write( "Node 10 is operational" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
