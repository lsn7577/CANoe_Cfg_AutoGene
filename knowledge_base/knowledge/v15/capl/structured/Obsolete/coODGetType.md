# coODGetType

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword coODGetType( dword index, dword subIndex, dword errCode[] ); |  |  |  |
| Function | The function returns the data type of an object in the local object dictionary. Note For the special file objects that are generated with the function coODCreate in order to read or write on the file system, internally the data type Domain is assumed. | Note For the special file objects that are generated with the function coODCreate in order to read or write on the file system, internally the data type Domain is assumed. |  |  |
| Note For the special file objects that are generated with the function coODCreate in order to read or write on the file system, internally the data type Domain is assumed. |  |  |  |  |
| Parameters | index Index of the object, value range 1..65.535 |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | Data type of the object |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];dword datatype;datatype= coODGetType( 0x1000, 0x0, errCode );if (errCode[0] == 0) { write( "Object data type: %d", datatype);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
