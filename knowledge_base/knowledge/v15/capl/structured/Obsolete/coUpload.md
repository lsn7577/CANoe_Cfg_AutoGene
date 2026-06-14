# coUpload

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coUpload( dword nodeId, dword index, dword subIndex, dword flags, dword errCode[] ); |  |  |  |
| Function | Reading of an entry from the object dictionary of another node. The function triggers a SDO upload. The response of the node is returned in the event function coOnUploadResponse or coOnError. |  |  |  |
| Parameters | nodeId Node-ID, value range 1..127 |  |  |  |
| index Index of the object, value range 1..65.535 |  |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| flags Bit field with options:0 - block transfer off1 - block transfer on |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coUpload( 1, 0x1000, 0x00, 0, errCode );if (errCode[0] == 0) { write( "SDO Upload successfully initiated" ); } |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
