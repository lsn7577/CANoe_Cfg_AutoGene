# coODCreateFloat

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coODCreateFloat( dword index, dword subIndex, dword dataType, dword access, float initValue, dword errCode[] ); |  |  |  |
| Function | Generates a new object in the local object dictionary of the specified type and with a floating point start value. If the size of the object (type 0x8 - 32 bit) is smaller than the length of the start value (64 bits), a conversion is undertaken. This can cause lower precision or value falsification. If the object already exists, then it is replaced by the new object. |  |  |  |
| Parameters | index Index of the object, value range 1..65.535 |  |  |  |
| subIndex Sub index of the object, value range 0..254 |  |  |  |  |
| dataType Data type of the object (limited, only type 0x8 and 0x11) |  |  |  |  |
| access Access type of the object |  |  |  |  |
| initValue Initial value of the object |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coODCreateFloat( 0x2000, 0x0, 0x8, 1, 2.5894, errCode );if (errCode[0] == 0) { write( "Object [0x2000,0] created" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
