# Enumeration

> Category: `Sensor` | Type: `notes`

## Description

eSensorOperationFailed

eSensorSendBufferFull

| Value | Enum | Short Description |
|---|---|---|
| 0 | eSensorNoError | The function call succeeded |
| 1 | eSensorFunctionNotSupported | The function is not supported on the given callee |
| 2 | eSensorInvalidArgument | One or more arguments had an invalid value |
| 3 | eSensorInvalidState | The callee is in a state that does not support the function call |
| 4 | eSensorDisturbanceNotSupported | The given disturbance is not supported on the callee |
| 5 | eSensorTargetNotFound | No callee with the given name was found |
| 6 | eSensorOperationFailed | An internal error occurred while processing the call |
| 7 | eSensorSendBufferFull | Operation failed because no free send buffer is available |

| Value | Enum | Short Description |
|---|---|---|
| 0 | ePsi5AutoCrc | CRC/parity field content is calculated and set automatically |
| 1 | ePsi5ManualCrc | CRC/parity field content is set as given in struct |
| 2 | ePsi5WrongCrc | CRC/parity field is set to a value that is explicitly wrong |

| Value | Enum | Short Description |
|---|---|---|
| 0 | eSentAutoCrc | CRC/parity field content is calculated and set automatically |
| 1 | eSentManualCrc | CRC/parity field content is set as given in struct |
| 2 | eSentWrongCrc | CRC/parity field is set to a value that is explicitly wrong |
| 3 | eSentRecommendedCrc | Explicitly uses the new, recommended CRC algorithm to calculate the CRC field content |
| 4 | eSentLegacyCrc | Explicitly uses the legacy CRC algorithm to calculate the CRC field content |

| Version 15© Vector Informatik GmbH |
|---|
