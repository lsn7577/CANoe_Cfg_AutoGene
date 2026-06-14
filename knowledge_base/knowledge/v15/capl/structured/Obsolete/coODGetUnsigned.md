# coODGetUnsigned

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dwordcoODGetUnsigned( dword index, dword subIndex, dword errCode[] ); |  |  |  |
| Function | Returns the value of an object in the local object dictionary without a leading sign. This function can be applied to all objects with a length up to 32 bits. Exceptions are the data type 0x8, 0x9, 0xA, 0xF, and 0x11. For the use of this function, a note on handling should be considered. |  |  |  |
| Parameters | index Index of the object, value range 1..65.535 |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | Value of the object |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];dword value;value = coODGetUnsigned( 0x2000, 0x0, errCode );if (errCode[0] == 0) { write( "Read value %d", value);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
