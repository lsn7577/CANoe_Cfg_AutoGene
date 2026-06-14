# ChkCreate_SignalValueChange, ChkStart_SignalValueChange

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_SignalValueChange (Signal aObservedSignal, char [] CaplCallback); // form 1
dword ChkStart_SignalValueChange (Signal aObservedSignal, char [] CaplCallback); // form 2
dword ChkCreate_SignalValueChange (EnvVar EnvVarName, char [] CaplCallback); // form 3
dword ChkStart_SignalValueChange (EnvVar EnvVarName, char [] CaplCallback); // form 4
dword ChkCreate_SignalValueChange (sysVar aSysVar, char [] CaplCallback); // form 5
dword ChkStart_SignalValueChange (sysVar aSysVar, char [] CaplCallback); // form 6
dword ChkCreate_SignalValueChange (valueHandle* doValue, char [] CaplCallback); // form 7
dword ChkStart_SignalValueChange (valueHandle* doValue, char [] CaplCallback); // form 8
dword ChkCreate_SignalValueChange (valueHandle* doValue, functionPointer Callback); // form 9
dword ChkStart_SignalValueChange (valueHandle* doValue, functionPointer Callback); // form 10
```

## Description

Checks the physical value of a signal or an environment variable.

An event will be generated, if the value will be changed.

## Parameters

| Name | Description |
|---|---|
| aObservedSignal | Signal to be checked. |
| EnvVarName | Environment variable to be checked. |
| CaplCallback | In simulation nodes this parameter has to be set.In test modules this parameter is optional. |
| aSysVar | System variable to be checked. |
| doValue | Distributed object member to be checked. |

## Example

Example 1

Example 2: CAPL Callback

Example 3: Function Pointer

```c
// checks that there is no change of the value of the signal
checkId = ChkStart_SignalValueChange (SignalToObserve);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
// checks that there is no change of the value of the signal
checkId = ChkStart_SignalValueChange (SignalToObserve, "CAPL_Callback");
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
...
void CAPL_Callback(dword check)
{
  write("Check id is %d", check);
}
// checks that there is no change of the value of the distributed object member
checkId = ChkStart_SignalValueChange (DOProvider.DoubleMember, delegate (dword check)
  {
    write("Check id is %d", check);
  });
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 7.0 SP5: method 8.5 SP3: form 5, 6 15: form 7-10 | 13.0: form 1-6 15: form 7-10 | — | 14: form 1-6 15: form 7-10 | 1.0: form 1-4 2.0 SP2: form 5, 6 6: form 7-10 |
| Restricted To | — | CAN LIN FlexRay A429 (since 8.5 SP4) | CAN LIN FlexRay A429 | — | CAN LIN FlexRay A429 | CAN LIN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
