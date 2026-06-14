# coGetNodeLabel

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coGetNodeLabel( char buffer[], dword bufferSize, dword errCode[] ); |  |  |  |
| Function | The function returns the label of the node. The label is formed from the name and the node-ID of the assigned database. Note So that the label of the node can be formed correctly, a few things must be noted. For more details, see Integration of the node layer in the introduction. | Note So that the label of the node can be formed correctly, a few things must be noted. For more details, see Integration of the node layer in the introduction. |  |  |
| Note So that the label of the node can be formed correctly, a few things must be noted. For more details, see Integration of the node layer in the introduction. |  |  |  |  |
| Parameters | buffer Buffer for the label |  |  |  |
| bufferSize Size of the buffer in bytes |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];char nodeLabel[256];coGetNodeLabel ( nodeLabel, elcount(nodeLabel), errCode );if (errCode[0] == 0) { write( "Nodelabel is: %s", nodeLabel );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
