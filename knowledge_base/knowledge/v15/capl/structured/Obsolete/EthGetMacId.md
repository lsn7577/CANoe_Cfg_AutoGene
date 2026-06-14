# EthGetMacId

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by IpGetAdapterMacId |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthGetMacId( byte macId[] ); |  |  |  |
| Function | This function reads the MAC-ID of the Ethernet interface. |  |  |  |
| Parameters | macId destination array for the read MAC-ID with six elements |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example on start { BYTE macId[6]; if (EthGetMacId( macId ) == 0) { write( "MAC ID is %.2X:%.2X:%.2X:%.2X:%.2X:%.2X:", macId[0], macId[1], macId[2], macId[3], macId[4], macId[5] ); }} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
