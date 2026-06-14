# coOnRPDOMissing

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coOnRPDOMissing( dword pdoNumber ); |  |  |  |
| Function | The function is called if an event timer of a RPDO is activated and the PDO is not received in the defined time. |  |  |  |
| Parameters | pdoNumber RPDO number 1..512 |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.0-9.0 SP6 | CANopen | — | • |  |
| Example void coOnRPDOMissing(dword pdoNumber){ write( "Receive PDO %d is missing", pdoNumber);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
