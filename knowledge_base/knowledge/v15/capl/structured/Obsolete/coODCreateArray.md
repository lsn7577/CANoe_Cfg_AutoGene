# coODCreateArray

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coODCreateArray( dword index, dword dataType, dword accessSub0, dword access, dword elementCount, dword errCode[] ); |  |  |  |
| Function | Generates a new field object in the local object dictionary. If the object already exists, then it is replaced by the new object. |  |  |  |
| Parameters | index Index of the object, value range 1..65.535 |  |  |  |
| dataType Data type of the object |  |  |  |  |
| accessSub0 Access type of the first sub object |  |  |  |  |
| access Access type of all additional sub objects |  |  |  |  |
| elementCount Number of elements of the field, value range 1..254 |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coODCreateArray( 0x1f81, 0x7, 0, 1, 127, errCode );if (errCode[0] == 0) { write( "Array [0x1f81] created" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
