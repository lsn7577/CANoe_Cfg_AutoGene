# ILNodeControlResume

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeControlResume(char aNodeName[]); // form 1
long ILNodeControlResume(char aNodeName[],dword flags); // form 2
```

## Description

Restarts the interaction layer of the specified simulation node. Cyclical sending of messages is restarted. The specified node must be in the current bus context. In all other cases the function has no effect and will return with an error.

## Parameters

| Name | Description |
|---|---|
| aNodeName | Name of the node of which the interaction layer should be started. |
| flags | 0: Signals/PDUs are sent with the last current values (of the latest updated buffer content). 1: Signals/PDUs are sent with Init value, corresponds to form 1. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3: form 1 9.0: form 2 | 14 | 14 | — | — |
| Restricted To | — | CAN FlexRay | CAN FlexRay | CAN FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
