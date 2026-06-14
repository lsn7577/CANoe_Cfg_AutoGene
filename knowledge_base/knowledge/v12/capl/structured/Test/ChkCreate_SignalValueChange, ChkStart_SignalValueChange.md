# ChkCreate_SignalValueChange, ChkStart_SignalValueChange

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_SignalValueChange (Signal aObservedSignal, char [] CaplCallback); // form 1
```

## Description

Checks the physical value of a signal or an environment variable.

An event will be generated, if the value will be changed.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks that there is no change of the value of the signal
checkId = ChkStart_SignalValueChange (SignalToObserve);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
