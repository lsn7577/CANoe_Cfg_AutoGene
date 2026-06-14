# coLssSwitchModeSel

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coLssSwitchModeSel( dword vendorId, dword productCode, dword revisionNo, dword serialNo, dword errCode[] ); |  |  |  |
| Function | This service puts the LSS slave whose LSS address matches the transmitted parameters into the configuration mode. |  |  |  |
| Parameters | vendorId Vendor-ID of the slave |  |  |  |
| productCode Product code of the slave |  |  |  |  |
| revisionNo Revision number of the slave |  |  |  |  |
| serialNo Serial number of the slave |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coLssSwitchModeSel( 0x1020304, 0x5060708, 0x90a0b0c, 0xd0e0f10, errCode );if (errCode[0] == 0) { write( "Switch to configuration mode for one slave commanded" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
