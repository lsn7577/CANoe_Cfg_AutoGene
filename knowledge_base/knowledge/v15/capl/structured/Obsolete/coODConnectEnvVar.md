# coODConnectEnvVar

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coODConnectEnvVar( dword index, dword subIndex, char envVar[], dword errCode[] ); |  |  |  |
| Function | Connects an object from the local object dictionary with an environment variable. |  |  |  |
| Parameters | index Index of the object, value range 1..65535 |  |  |  |
| subIndex Sub index of the object, value range 0..255 |  |  |  |  |
| envVar Name of the environment variable |  |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];char errBuffer[128];coODConnectEnvVar( 0x6000, 0x1, "MyEnvVar", errCode );if(errCode[0] != 0) { coGetLastError(errBuffer, elCount(errBuffer)); write( "coODConnectEnvVar failed with code: %x - %s", errCode[0], errBuffer);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
