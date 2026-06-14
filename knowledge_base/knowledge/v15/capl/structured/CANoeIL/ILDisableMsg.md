# ILDisableMsg

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILDisableMsg (char msgName[])
```

## Description

Disables the sending of the message except by calling the function ILSetMsgEvent.

## Parameters

| Name | Description |
|---|---|
| msgName | Message that should be disabled. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP2 | 14 | 14 | — | — |
| Restricted To | — | CAN Simulation Nodes | CAN Simulation Nodes | CAN Simulation Nodes | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
