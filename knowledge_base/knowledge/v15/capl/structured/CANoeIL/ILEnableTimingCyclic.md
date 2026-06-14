# ILEnableTimingCyclic

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILEnableTimingCyclic(char pduName[], int enable)
```

## Description

Controls the cyclic timing of PDUs. The cyclic timing can be enabled/disabled.This function influences a simulation node with an assigned CANoe interaction layer.

## Parameters

| Name | Description |
|---|---|
| aPDUName | Name of the PDU that should be modified. |
| enable | 0 = disable1 = enable |

## Example

```c
// Disables the PDU Timing for 2000 ms

variables {
  int enable = 0;
  msTimer WaitTimer;
}

on key 'a'{
  enable = 0;
  ILEnableTimingCyclic ("PDU_A", enable);
  SetTimer(WaitTimer,2000);
}

on Timer WaitTimer {
  enable = 1;
  ILEnableTimingCyclic ("PDU_A", enable);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 14 | 14 | — | — |
| Restricted To | — | FlexRay Simulation nodes | FlexRay Simulation nodes | FlexRay Simulation nodes | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
