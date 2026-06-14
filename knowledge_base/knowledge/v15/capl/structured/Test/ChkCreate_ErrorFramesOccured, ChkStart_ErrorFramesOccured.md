# ChkCreate_ErrorFramesOccured, ChkStart_ErrorFramesOccured

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_ErrorFramesOccured (long MinCountOfErrorFrames, long MaxCountOfErrorFrames, dword Timeout, char CaplCallbackFunction[]);
dword ChkStart_ErrorFramesOccured (long MinCountOfErrorFrames, long MaxCountOfErrorFrames, dword Timeout, char CaplCallbackFunction[]);
dword ChkCreate_ErrorFramesOccured (char CaplCallbackFunction[]);
dword ChkStart_ErrorFramesOccured (char CaplCallbackFunction[]);
dword ChkCreate_ErrorFramesOccured (long MinCountOfErrorFrames, long MaxCountOfErrorFrames, dword Timeout);
dword ChkStart_ErrorFramesOccured (long MinCountOfErrorFrames, long MaxCountOfErrorFrames, dword Timeout);
dword ChkCreate_ErrorFramesOccured ();
dword ChkStart_ErrorFramesOccured ();
```

## Description

Checks the occurrence of Error Frames on the bus. The event is generated if fewer than MinCountOfErrorFrames or more than MaxCountOfErrorFrames are received.

The minimum condition is only checked when 'Timeout != 0'

## Parameters

| Name | Description |
|---|---|
| MinCountOfErrorFrames | Minimum number of Error Frames that must be received.This parameter is set to 0 in signatures without parameter. Only check when 'Timeout != 0' |
| MaxCountOfErrorFrames | Maximum number of Error Frames that may occur.This parameter is set to 0 in signatures without parameter. |
| Timeout | The check is automatically stopped after this time. The check is no longer in progress. If the timeout is specified with zero, it behaves like all other checks. It runs until the ChkControl_Stop(id) function is called. Default unit [ms], if not changed with ChkConfig_SetPrecision. |
| CaplCallbackFunction | In simulation nodes this parameter has to be set.In test modules this parameter is optional. |

## Example

```c
// observes that less than 3 Error Frames occurs
checkId = ChkStart_ErrorFramesOccured (0, 2, 0);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN | CAN | — | CAN | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
