# coSetBlockSize

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coSetBlockSize( dword blockSize, dword errCode[] ); |  |  |  |
| Function | This function sets the block size that is used for SDO block transfers. The default value is 7 and applies globally for all SDO transmission. |  |  |  |
| Parameters | blockSize Block size to be used for SDO block transfers, 1..127 |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coSetBlockSize( 14, errCode );if (errCode[0] == 0) { write( "SDO block size successfully set" ); } |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
