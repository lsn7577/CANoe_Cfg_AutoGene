# linSetRespTolerance

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetRespTolerance(long frameId, long toleranceInPercent);
```

## Description

Sets the response tolerance for a specified frame in percent.

## Parameters

| Name | Description |
|---|---|
| frameId | The identifier of the frame for which the response tolerance shall be set. |
| toleranceInPercent | The response tolerance to be used for the specified frame. Value range: 0-255 |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 | 7.0 | — | — | — | 1.0 |
| Restricted To | LIN Real bus mode | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
