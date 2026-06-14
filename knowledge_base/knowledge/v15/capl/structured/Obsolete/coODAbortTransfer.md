# coODAbortTransfer

> Category: `Obsolete` | Type: `notes`

## Description

This function is only available in the event functions (callbacks).

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Note This function is only available in the event functions (callbacks). |  |  |  |  |
| Function Syntax | void coODAbortTransfer( dword abortCode, dword errCode[] ); |  |  |  |
| Function | The function aborts a SDO transfer, which was initiated on an object with access type 7. It can be used in the event functions coOnDownloadIndication or coOnUploadIndication. |  |  |  |
| Parameters | abortCode Abort code of the SDO transfer (see /3/ or coOnError under error class 3, except 0xFF01...) |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example void coOnUploadIndication (dword index, dword subIndex) { dword errCode[1]; if (index > 0x2003) {coODAbortTransfer( 0x06020000, errCode ); // object doesn't exist if (errCode[0] == 0) { write( "Aborting SDO transfer successfully initiated" ); } }} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
