# coThisGetSize

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword coThisGetSize( dword errCode[] ); |  |  |  |
| Function | The function returns the size of the data of a SDO transfer in the event function coOnUploadResponse or coOnDownloadIndication. The call is only allowed in this event function. |  |  |  |
| Parameters | errCode Error code buffer (is entered in index 0 of the field) |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];dword size;size = coThisGetSize( errCode ); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
