# coODSetFloat

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coODSetFloat( dword index, dword subIndex, float value, dword errCode[] ); |  |  |  |
| Function | Sets the floating point value of an object in the local object dictionary. This function can only be applied to objects with the data types 0x8 and 0x11. For the use of this function, a note on handling should be considered. |  |  |  |
| Parameters | index Index of the object, value range 1..65.535 |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| value Value of the object Note Since CAPL only supports 8 byte floating point numbers, note that the value range must not be left when writing to a Real32 object. | Note Since CAPL only supports 8 byte floating point numbers, note that the value range must not be left when writing to a Real32 object. |  |  |  |
| Note Since CAPL only supports 8 byte floating point numbers, note that the value range must not be left when writing to a Real32 object. |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coODSetFloat( 0x2000, 0x0, 123.456789, errCode );if (errCode[0] == 0) { write( "New object value successfully set");} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
