# coThisGetUnsigned

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword coThisGetUnsigned( dword errCode[] ); |  |  |  |
| Function | The function returns a value with no leading sign of an object in the event functions coOnUploadResponse or coOnDownloadIndication. The call is only allowed in these event functions. |  |  |  |
| Parameters | errCode Error code buffer (is entered in index 0 of the field) |  |  |  |
| Return Values | Value of the object entry |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];dword value;value = coThisGetUnsigned( errCode ); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
