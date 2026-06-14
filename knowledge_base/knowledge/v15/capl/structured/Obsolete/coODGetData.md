# coODGetData

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword coODGetData( dword index, dword subIndex, char buffer[], dword bufferSize, dword errCode[] ); |  |  |  |
| dword coODGetData( dword index, dword subIndex, byte buffer[], dword bufferSize, dword errCode[] ); |  |  |  |  |
| Function | Returns the data of an object in the local object dictionary. This function can be applied to all objects. For objects with a size up to 32 bits or floating point objects, however, the functions coODGetSigned, coODGetUnsigned, and coODGetFloat are recommended. For the use of this function, a note on handling should be considered. |  |  |  |
| Parameters | index Index of the object, value range 1..65.535 |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| buffer Buffer for the read data |  |  |  |  |
| bufferSize Size of the buffer in bytes |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | Number of read data bytes |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];char buffer[128];dword count;count = coODGetData( 0x1008, 0x0, buffer, elCount(buffer), errCode );if (errCode[0] == 0) { write( "Object size %d, object data %s", count, buffer);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
