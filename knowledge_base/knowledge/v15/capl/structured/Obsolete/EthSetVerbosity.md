# EthSetVerbosity

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: — |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthSetVerbosity( long verbosity); |  |  |  |
| Function | This function set the verbosity level of the Ethernet IL. The default setting is that only error messages are written to the Write Window of CANoe. |  |  |  |
| Parameters | verbosity verbosity level 0: do not write messages to the Write Window 1: write only error messages (default) 2: write warning and error messages 3: write information, warning and error messages |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example // do not print Ethernet IL messages to Write WindowEthSetVerbosity( 0 ); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
