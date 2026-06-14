# ChkQuery_EventStatus

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventStatus (dword aCheckId, char aBuffer[], dword aBufferLength);
```

## Description

Converts the status into a string that can be printed. Returns the number of characters written (<= length).

## Parameters

| Name | Description |
|---|---|
| aCheckId | — |
| aBuffer | — |
| aBufferLength | — |

## Example

```c
long result;
dword checkId;
char eventStatus[256];
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_EventStatus(checkId, eventStatus, 256);
Write("result = %d", result);
Write("Event Status = %s", eventStatus);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
