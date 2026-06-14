# coODSetSigned

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coODSetSigned( dword index, dword subIndex, long value, dword errCode[] ); |  |  |  |
| Function | Sets the value of an object in the local object dictionary with a leading sign. This function can only be applied to objects with the data types 0x2, 0x3, 0x10, and 0x4. For the use of this function, a note on handling should be considered. |  |  |  |
| Parameters | index Index of the object, value range 1..65.535 |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| value Value of the object |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coODSetSigned( 0x2000, 0x0, -789, errCode );if (errCode[0] == 0) { write( "New object value successfully set");} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
