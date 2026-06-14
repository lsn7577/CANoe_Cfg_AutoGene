# coODGetSize

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword coODGetSize( dword index, dword subIndex, dword errCode[] ); |  |  |  |
| Function | The function returns the size of an object in the local object dictionary in bytes. |  |  |  |
| Parameters | index Index of the object, value range 1..65.535 |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | Size of the object in bytes |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];dword size;size = coODGetSize( 0x1000, 0x0, errCode );if (errCode[0] == 0) { write( "Object size: %d byte", size);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
