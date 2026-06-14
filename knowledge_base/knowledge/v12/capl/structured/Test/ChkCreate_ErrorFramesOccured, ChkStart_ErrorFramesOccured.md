# ChkCreate_ErrorFramesOccured, ChkStart_ErrorFramesOccured

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_ErrorFramesOccured (long MinCountOfErrorFrames, long MaxCountOfErrorFrames, dword Timeout, char CaplCallbackFunction[]);
```

## Description

Checks the occurrence of Error Frames on the bus. The event is generated if fewer than MinCountOfErrorFrames or more than MaxCountOfErrorFrames are received.

The minimum condition is only checked when 'Timeout != 0'

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

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

| Since Version |
|---|
