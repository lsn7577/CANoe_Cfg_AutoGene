# ChkCreate_BurstTimeLimitViolation, ChkStart_BurstTimeLimitViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_BurstTimeLimitViolation (char[] aBusName, duration aMaxTime);
dword ChkStart_BurstTimeLimitViolation (char[] aBusName, duration aMaxTime);
```

## Description

Checks the maximum burst time on a bus.

## Parameters

| Name | Description |
|---|---|
| aBusName | Name of the bus. |
| aMaxTime | Maximum burst time. Default unit [ms], if not changed with ChkConfig_SetPrecision. |

## Example

```c
// observes the maximum burst time 3 ms
checkId = ChkStart_BurstTimeLimitViolation ("CAN", 3);
TestAddCondition(checkId);

// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN | CAN | — | CAN | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
