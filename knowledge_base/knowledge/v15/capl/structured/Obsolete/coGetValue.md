# coGetValue

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long coGetValue( char envVar[], dword errCode[] ); |  |  |  |
| Function | The function returns the current value of an environment variable of the type integer. Note In contrast to the getValue function of CANoe, with this function the name for runtime can be specified via a string and it does not already have to be known at translation time. This means, for example, it can be combined at runtime with the help of string functions. | Note In contrast to the getValue function of CANoe, with this function the name for runtime can be specified via a string and it does not already have to be known at translation time. This means, for example, it can be combined at runtime with the help of string functions. |  |  |
| Note In contrast to the getValue function of CANoe, with this function the name for runtime can be specified via a string and it does not already have to be known at translation time. This means, for example, it can be combined at runtime with the help of string functions. |  |  |  |  |
| Parameters | envVar Name of the environment variable |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | Value of the environment variable |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];long returnValue ;returnValue = coGetValue("envVarStart", errCode);if (errCode[0] == 0) { write( "Value of the environment variable is: %d", returnValue );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
