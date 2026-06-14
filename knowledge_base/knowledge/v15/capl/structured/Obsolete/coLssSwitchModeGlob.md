# coLssSwitchModeGlob

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coLssSwitchModeGlob( dword mode, dword errCode[] ); |  |  |  |
| Function | Change of all LSS slaves into the configuration mode or leaving of the mode. |  |  |  |
| Parameters | mode Specifies in which mode all LSS slaves are switched 0 - leaving of the configuration mode1 - transition to the configuration mode |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coLssSwitchModeGlob( 1, errCode );if (errCode[0] == 0) { write( "Switch to configuration mode for all slaves commanded" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
