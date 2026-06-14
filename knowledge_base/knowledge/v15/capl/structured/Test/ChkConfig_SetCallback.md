# ChkConfig_SetCallback

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkConfig_SetCallback(dword aCheckId, char [] CaplCallback);
```

## Description

Sets a CAPL callback for the check. An already existing callback will be overwritten.This function can be used if the check itself has no syntax to create/start and to assign a callback.

## Parameters

| Name | Description |
|---|---|
| aCheckId | Must exist |
| CaplCallback | The name of the CAPL callback function. |

## Example

```c
void callback(dword id)
{
  // do something
}
testcase TC1()
{
  int checkId;

  checkId = ChkCreate_MsgOccurrenceCount(MsgA1, 3);

  testAddCondition(checkId);
  ChkConfig_SetCallback(checkId, "callback");
  ChkControl_Start(checkId);

  testWaitForTimeout(3000);

  ChkControl_Stop(checkId);
  testRemoveCondition(checkId);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP2 | 13.0 | — | 14 | 2.2 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
