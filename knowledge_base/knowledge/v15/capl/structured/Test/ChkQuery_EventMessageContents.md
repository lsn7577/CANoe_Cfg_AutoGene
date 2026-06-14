# ChkQuery_EventMessageContents

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventMessageContents (dword CheckId, byte buffer[], dword bufferlen);
```

## Description

Stores the data bytes of the message, for which the event has been sent, in the buffer and returns the number of stored data bytes (DLC).

## Parameters

| Name | Description |
|---|---|
| CheckId | Identifier of the queried Check. |
| buffer | — |
| bufferlen | — |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | LIN | LIN | — | LIN | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
