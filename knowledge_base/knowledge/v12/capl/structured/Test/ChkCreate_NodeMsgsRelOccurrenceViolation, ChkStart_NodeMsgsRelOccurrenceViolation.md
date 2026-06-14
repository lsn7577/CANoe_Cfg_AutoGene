# ChkCreate_NodeMsgsRelOccurrenceViolation, ChkStart_NodeMsgsRelOccurrenceViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_NodeMsgsRelOccurrenceViolation(Node observedNode, double aMinRelCycleTime, double aMaxRelCycleTime, char[] aCallback);
```

## Description

Checks for the occurrence of periodic message of the specified send node.The check condition is violated if the time between transmissions of the message is less than aMinRelCycleTime * GenMsgDelayTime or greater than aMaxRelCycleTime * Cycle Time.Cycle time is calculated from GenMsgCycleTime and GenSigCycleTime.Limits that should not be checked must be set to 0. At least one limit must be specified.Can only be started in the "on start" area of CAPL or during the measurement. However, the check may be set up as early as in the "pre start" area.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks the periodic occurrence of all messages of the node
checkId = ChkStart_NodeMsgsRelOccurrenceViolation (NodeToObserve, 0.9, 1.1);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
