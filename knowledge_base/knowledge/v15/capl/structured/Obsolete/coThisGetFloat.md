# coThisGetFloat

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | float coThisGetFloat( dword errCode[] ); |  |  |  |
| Function | The function returns a floating point value of an object in the event functions coOnUploadResponse or coOnDownloadIndication. The call is only allowed in these event functions. |  |  |  |
| Parameters | errCode Error code buffer (is entered in index 0 of the field) |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];float value;value = coThisGetFloat( errCode ); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
