# coOnDownloadResponse

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coOnDownloadResponse( dword nodeId, dword index, dword subIndex ); |  |  |  |
| Function | This function is called if the response to a SDO download was received (see coDownload and coDownloadExpedited ). |  |  |  |
| Parameters | nodeId Node-ID, value range 1..127 |  |  |  |
| index Index of the object, value range 1..65.535 |  |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example void coOnDownloadResponse( dword nodeId, dword index, dword subIndex ){ write( "Download response of [0x%.4x,0x%.2x] from node %d received", index, subIndex, nodeId );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
