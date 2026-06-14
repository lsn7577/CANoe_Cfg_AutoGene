# ILSetOperationMode

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILSetOperationMode(long mode, long param); // form 1
long ILSetOperationMode(dbMsg message, char signalGroupName[], long mode, long param); // form 2
long ILSetOperationMode(dbSignal signal, long mode, long param); // form 3
```

## Description

Form 1:

Sets specific operation mode in the interaction layer of the specified simulation node. The specified node must be in the current bus context. In all other cases the function has no effect and will return with an error.

Form 2:

Sets specific operation mode in the interaction layer for the specified signal group of the specified message.

Form 3:

Sets specific operation mode in the interaction layer for the specified signal.

## Parameters

| Name | Description |
|---|---|
| aNodeName | Name of the node of which the specific operation mode should be set. |
| signalGroupName | Name of the signal group. |
| message | Message of which the specific operation mode should be set. |
| signal | Name of the update bit signal of which the specific operation mode should be set. |
| mode | 0: Influences update bits. Thus, the OEM should support update bits. How the operation of setting update bits is manipulated defines the second parameter, see below. Other values are reserved. |
| Syntax Form | Mode Value Param Value Description |
| 1 | 0 0 All update bits will be set or reset depending on the signal updates |
| 1 | All update bits will always be sent with value = 1 |
| 2 | 0 0 The update bit of the signal group will be set or reset depending on the signal updates |
| 1 | The update bit of the signal group will always be sent with value = 1 |
| 3 | 0 0 The update bit will be set or reset depending on the signal updates |
| 1 | The update bit will always be sent with value = 1 |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | 13.0 | — | 14 | —✔ |
| Restricted To | — | CAN FlexRay | CAN FlexRay | — | CAN FlexRay | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | —✔ |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | —✔ |
| 64-Bit | — | ✔ | ✔ | — | ✔ | —✔ |
