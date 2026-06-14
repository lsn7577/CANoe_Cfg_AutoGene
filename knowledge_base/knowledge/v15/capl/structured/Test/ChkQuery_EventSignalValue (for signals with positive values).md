# ChkQuery_EventSignalValue (for signals with positive values)

> Category: `Test` | Type: `function`

## Syntax

```c
double ChkQuery_EventSignalValue (dword checkId);
```

## Description

This function enables access to the signal value which was last reported by a check as invalid.

This function enables access only to positive signal values.

## Parameters

| Name | Description |
|---|---|
| checkId | Identifier of the queried Check. |

## Example

```c
double result;
dword checkId;
checkId = ChkStart_MsgSignalValueInvalid(Velocity, 80, 100);
// ... execute test sequence
result = ChkQuery_EventSignalValue(checkId);
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
