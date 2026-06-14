# ChkCreate_MsgSignalValueInvalid, ChkStart_MsgSignalValueInvalid

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MsgSignalValueInvalid (Signal aObservedSignal, double aMinValue, double aMaxValue, Callback aCallback); // form 1
```

## Description

Check the value of a signal, of an environment variable or a system variable. The value should be outside the given value range (inclusive limits).

An event will be generated, if the value of the physical signal, the environment variable or the system variable is inside the given value range.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Example

```c
// checks the value of the signal (should be outside the given range)
checkId = ChkStart_MsgSignalValueInvalid (SignalToObserve, 2.5, 3.7);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
