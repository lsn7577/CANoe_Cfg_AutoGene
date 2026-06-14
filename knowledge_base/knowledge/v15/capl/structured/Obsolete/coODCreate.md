# coODCreate

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coODCreate( dword index, dword subIndex, dword dataType, dword access, dword errCode[] ); // form 1 |  |  |  |
| void coODCreate( dword index, dword subIndex, dword dataType, dword access, byte initData[], dword dataSize, dword errCode[] ); // form 2 |  |  |  |  |
| void coODCreate( dword index, dword subIndex, dword access, char filename[], dword errCode[] ); // form 3 |  |  |  |  |
| Function | Generates a new object in the local object dictionary. If the object already exists, it is replaced by the new object. Form 1 generates a new object of the specified type and without a start value. The value of the object is initialized with null. Form 2 generates a new object of the specified type with the specified initial data. If the length of the available start data is smaller than the size of the object, the remaining part is initialized with null. Form 3 generates a new special object, with the internally assumed data type Domain. This object reads from and/or writes to a file on the local file system. |  |  |  |
| Parameters | index Index of the object, value range 1..65.535 |  |  |  |
| subIndex Sub index of the object, value range 0..254 |  |  |  |  |
| dataType data type of the object |  |  |  |  |
| Access access type of the object, if form (3) is used, the access type is limited to 0..2 |  |  |  |  |
| initData Initial data of the object |  |  |  |  |
| dataSize Length of the initial data in bytes |  |  |  |  |
| filename Path and name of the file (absolute or relative to the CANoe configuration) |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];char data[10] = "myDevice";// manufacturer device namecoODCreate( 0x1008, 0x0, 0x9, 0, data, elCount(data), errCode );if (errCode[0] == 0) { write( "String object [0x1008] created" );}coODCreate( 0x2000, 0x0, 1, "./myFile.txt", errCode );if (errCode[0] == 0) { write( "File object [0x2000] created" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
