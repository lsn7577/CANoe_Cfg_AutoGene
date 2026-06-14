# TestJoinFrStartCycleEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinFrStartCycleEvent (dword aCycle)
long TestJoinFrStartCycleEvent (dword aBaseCycle, dword aCycleRepetition)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

## Parameters

| Name | Description |
|---|---|
| aCycle | Numeric cycle identifier. Value range: 0...63 |
| aBaseCycle | Numeric base cycle. This value must be less than the repetition factor. Together with the repetition factor this value determines the "Cycle Multiplexing". Value range: 0...63 |
| aCycleRepetition | Cycle repetition factor. Together with the base cycle this value determines the "Cycle Multiplexing". Value has to be a power to 2 (1, 2, 4, 8, 16, 32 or 64). |

## Example

For an example see function TestWaitForFrStartCycle.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP4 | 13.0 | — | — | 1.0 |
| Restricted To | — | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
