# coSetSDOTimeout

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coSetSDOTimeout( dword time, dword errCode[] ); |  |  |  |
| Function | The function sets the time after which a SDO transmission is aborted if the communication partner does not response. The default value is 2000 ms and applies globally for all SDO transmission. |  |  |  |
| Parameters | time Time value in ms, value range 0..60000 |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coSetSDOTimeout( 100, errCode );if (errCode[0] == 0) { write( "SDO time-out set to 100ms" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
