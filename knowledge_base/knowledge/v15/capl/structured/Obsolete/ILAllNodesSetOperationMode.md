# ILAllNodesSetOperationMode

> Category: `Obsolete` | Type: `notes`

## Description

Sets specific operation mode in the interaction layer of all nodes in the current bus context.

8.2 SP3

| Deprecated Function This function is deprecated and has been replaced by ILNodeSetAllNodesOperationMode |  |  |  |  |
|---|---|---|---|---|
| Note This function is not available for all OEM packages — depends on the CANoeIL. This function can be used in a global node outside the node context of the IL and in test modules. |  |  |  |  |
| Function Syntax | long ILAllNodesSetOperationMode(long mode, long param) |  |  |  |
| Function | Sets specific operation mode in the interaction layer of all nodes in the current bus context. |  |  |  |
| Parameters | mode mode - 0: influences update bits; other values have currently no effect and are reserved. |  |  |  |
| param The effect of param depends on the parameter mode: Mode Value Param Value 0 0: all update bits will be set or reset depending on the signal updates 1: all update bits will always be sent with value = 1 | Mode Value | Param Value | 0 | 0: all update bits will be set or reset depending on the signal updates 1: all update bits will always be sent with value = 1 |
| Mode Value | Param Value |  |  |  |
| 0 | 0: all update bits will be set or reset depending on the signal updates 1: all update bits will always be sent with value = 1 |  |  |  |
| Return Values | 0: No error |  |  |  |
| -10000: Unspecific error |  |  |  |  |
| -10001: Node or module not found |  |  |  |  |
| -10002: No suitable module available |  |  |  |  |
| -10003: Function is not supported by module |  |  |  |  |
| -10004: Module returns illegal value |  |  |  |  |
| other: Error in module |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP3 | CAN FlexRay | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
