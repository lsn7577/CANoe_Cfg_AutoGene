# setDrift

> Category: `Other` | Type: `function`

## Syntax

```c
void setDrift(int drift);
```

## Description

A constant deviation can be set for the timers of a network node with this function. Inputs for the two values may lie between –10000 and 10000 (corresponds to –100.00% to 100.00%). If the value does not lie within this range, a message is output in the Write Window.

## Parameters

| Name | Description |
|---|---|
| drift | Integer for the constant deviation. |

## Return Values

—

## Example

```c
...
// Sets the Drift to 35.5 percent
setDrift(3550);
...
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 3.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
