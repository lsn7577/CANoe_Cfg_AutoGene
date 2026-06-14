# coODSetData

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coODSetData( dword index, dword subIndex, char data[], dword dataSize, dword errCode[] ); |  |  |  |
| void coODSetData( dword index, dword subIndex, byte data[], dword dataSize, dword errCode[] ); |  |  |  |  |
| Function | Sets the data of an object in the local object dictionary. This function can be applied to all objects. For objects with a size up to 32 bits or floating point objects, however, the functions coODSetSigned, coODSetUnsigned, and coODSetFloat are recommended. For the use of this function, a note on handling should be considered. |  |  |  |
| Parameters | index Index of the object, value range 1..65.535 |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| data Data of the object |  |  |  |  |
| dataSize Number of data bytes |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];char data[6] = { 1, 2, 3, 4, 5, 6 };coODSetData( 0x2000, 0x0, data, elCount(data), errCode );if (errCode[0] == 0) { write( "Object data successfully written");} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
