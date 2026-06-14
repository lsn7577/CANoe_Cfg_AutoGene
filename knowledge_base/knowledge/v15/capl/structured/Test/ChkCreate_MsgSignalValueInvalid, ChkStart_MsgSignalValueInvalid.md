# ChkCreate_MsgSignalValueInvalid, ChkStart_MsgSignalValueInvalid

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MsgSignalValueInvalid (Signal aObservedSignal, double aMinValue, double aMaxValue, char [] aCallback); // form 1
dword ChkStart_MsgSignalValueInvalid (Signal aObservedSignal, double aMinValue, double aMaxValue, char [] aCallback); // form 2
dword ChkCreate_MsgSignalValueInvalid (char aMessageName[], char aSignalName[], double aMinValue, double aMaxValue, char [] aCallback); // form 3
dword ChkStart_MsgSignalValueInvalid (char aMessageName[], char aSignalName[], double aMinValue, double aMaxValue, char [] aCallback); // form 4
dword ChkCreate_MsgSignalValueInvalid (EnvVarName, double aMinValue, double aMaxValue, char [] aCallback); // form 5
dword ChkStart_MsgSignalValueInvalid (EnvVarName, double aMinValue, double aMaxValue, char [] aCallback); // form 6
dword ChkCreate_MsgSignalValueInvalid (sysVar aSysVar, double aMinValue, double aMaxValue, char [] aCallback); // form 7
dword ChkStart_MsgSignalValueInvalid (sysVar aSysVar, double aMinValue, double aMaxValue, char [] aCallback); // form 8
dword ChkCreate_MsgSignalValueInvalid (sysVar aSysVar, int64 aMinValue, int64 aMaxValue, char [] aCallback); // form 9
dword ChkStart_MsgSignalValueInvalid (sysVar aSysVar, int64 aMin-Value, int64 aMaxValue, char [] aCallback); // form 10
dword ChkCreate_MsgSignalValueInvalid (valueHandle* doValue, double aMinValue, double aMaxValue, char [] aCallback); // form 11
dword ChkStart_MsgSignalValueInvalid (valueHandle* doValue, double aMinValue, double aMaxValue, char [] aCallback); // form 12
dword ChkCreate_MsgSignalValueInvalid (valueHandle* doValue, int64 aMinValue, int64 aMaxValue, char [] aCallback); // form 13
dword ChkStart_MsgSignalValueInvalid (valueHandle* doValue, int64 aMinValue, int64 aMaxValue, char [] aCallback); // form 14
dword ChkCreate_MsgSignalValueInvalid (valueHandle* doValue, double aMinValue, double aMaxValue, functionPointer Callback); // form 15
dword ChkStart_MsgSignalValueInvalid (valueHandle* doValue, double aMinValue, double aMaxValue, functionPointer Callback); // form 16
dword ChkCreate_MsgSignalValueInvalid (valueHandle* doValue, int64 aMinValue, int64 aMaxValue, functionPointer Callback); // form 17
dword ChkStart_MsgSignalValueInvalid (valueHandle* doValue, int64 aMinValue, int64 aMaxValue, functionPointer Callback); // form 18
```

## Description

Check the value of a signal, of an environment variable or a system variable. The value should be outside the given value range (inclusive limits).

An event will be generated, if the value of the physical signal, the environment variable or the system variable is inside the given value range.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Example

Example 1

Example 2: CAPL Callback

Example 3:Function Pointer

```c
// checks the value of the signal (should be outside the given range)
checkId = ChkStart_MsgSignalValueInvalid (SignalToObserve, 2.5, 3.7);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
// checks the value of the signal (should be outside the given range)
checkId = ChkStart_MsgSignalValueInvalid (SignalToObserve, 2.5, 3.7, "CAPL_Callback");
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
...
void CAPL_Callback(dword check)
{
  write("Check id is %d", check);
}
// checks the value of the distributed object member (should be outside the given range)
checkId = ChkStart_MsgSignalValueInvalid (DOProvider.DoubleMember, 2.5, 3.7, delegate (dword check)
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
| Since Version | — | 5.0: form 1-4 6.0: form 5-6 7.0 SP5: methods 1-6 7.2 SP3: form 7-8 8.5 SP3: form 9, 10 15: form 11-18 | 13.0: form 1-10 6: form 11-18 | — | 14: form 1-10 6: form 11-18 | 1.0: form 1-8 2.0 SP2: form 9, 10 6: form 11-18 |
| Restricted To | — | — | — | — | — | CAN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
