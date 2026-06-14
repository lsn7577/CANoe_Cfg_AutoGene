# ChkCreate_Timeout, ChkStart_Timeout

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_Timeout (Duration aTimeout, char [] CaplCallback);
dword ChkStart_Timeout (Duration aTimeout, char [] CaplCallback);
```

## Description

The check fires an event if the time has expired.

## Parameters

| Name | Description |
|---|---|
| aTimeout | > 0; default unit [ms], if not changed with ChkConfig_SetPrecision. |
| CaplCallback | In simulation nodes this parameter has to be set.In test modules this parameter is optional. |

## Example

```c
// checks the maximum duration of a sequence of actions
checkId = ChkStart_Timeout (2000);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | Test modules | Test modules | — | Test modules | Test module |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
