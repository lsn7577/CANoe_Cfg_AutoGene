# ILNodeSetOperationMode

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeSetOperationMode(char aNodeName[], long mode, long param); // form 1
long ILNodeSetOperationMode(dbMsg message, char signalGroupName[], long mode, long param); //(2)
long ILNodeSetOperationMode(dbSignal signal, long mode, long param); // form 3
```

## Description

Form 1:Sets specific operation mode in the interaction layer of the specified simulation node. The specified node must be in the current bus context. In all other cases the function has no effect and will return with an error.

Form 2:Sets specific operation mode in the interaction layer for the specified signal group of the specified message.

Form 3:Sets specific operation mode in the interaction layer for the specified signal.

## Parameters

| Name | Type | Description |
|---|---|---|
| aNodeName |  | Name of the node of which the specific operation mode should be set. Supported qualification patterns for form 1: [DBName::]aNodeName |
| signalGroupName |  | Name of the signal group. |
| message |  | Message of which the specific operation mode should be set. |
| signal |  | Name of the update bit signal of which the specific operation mode should be set. |
| mode |  | mode - 0: influences update bits; other values have currently no effect and are reserved. |
| Syntax form | Mode Value | Param Value |
| 1 | 0 | 0: all update bits will be set or reset depending on the signal updates 1: all update bits will always be sent with value = 1 |
| 2 | 0 | 0: the update bit of the signal group will be set or reset depending on the signal updates 1: the update bit of the signal group will always be sent with value = 1 |
| 3 | 0 | 0: the update bit will be set or reset depending on the signal updates 1: the update bit will always be sent with value = 1 |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | 14 | 14 | — | — |
| Restricted To | — | CAN FlexRay | CAN FlexRay | CAN FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
