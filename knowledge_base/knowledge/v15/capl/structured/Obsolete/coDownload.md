# coDownload

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coDownload( dword nodeId, dword index, dword subIndex, char data[], dword dataSize, dword flags, dword errCode[] ); |  |  |  |
| void coDownload( dword nodeId, dword index, dword subIndex, byte data[], dword dataSize, dword flags, dword errCode[] ); // form 2 |  |  |  |  |
| void coDownload( dword nodeId, dword index, dword subIndex, float value, dword flags, dword errCode[] ); // form 3 |  |  |  |  |
| Function | Writing of an entry into the object dictionary of another node. The function triggers a SDO download. The response of the node is returned in the event function coOnDownloadResponse or coOnError. (3) If it is used with the float parameter value, it always initiates a transfer with the length 8 bytes. This corresponds to the data type Real64. |  |  |  |
| Parameters | nodeId Node-ID, value range 1..127 |  |  |  |
| index Index of the object, value range 1..65.535 |  |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| data Data of the object |  |  |  |  |
| dataSize Number of data bytes |  |  |  |  |
| value Value of the object |  |  |  |  |
| flags Bit field with options:0 - block transfer off1 - block transfer on |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];char data[256] = "coDownloadData";coDownload( 1, 0x2000, 0x00, data, strlen(data), 0, errCode );if (errCode[0] == 0) { write( "SDO Download successfully initiated" ); } |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
