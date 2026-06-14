# ChkCreate_NodeMsgsAbsDistViolation, ChkStart_ NodeMsgsAbsDistViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_NodeMsgsAbsDistViolation (Node aNode, Duration aMinTime, long aViolationsMaxCount, Duration aRatingPeriod);
```

## Description

This check allows the supervision of the minimum send distance of all Tx messages of a node on one bus.

If no rating period and maximal number of distance undercuts is specified, the check condition fails if the time interval between two messages of the node undercuts the MinTime.

If the rating period and the maximal number of distance undercuts (> 0) are specified, the check observes the number of distance undercuts in a time slot. Exceeds the number of distance undercuts the allowed number in a time slot, the check fails.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks the send distance between all Tx messages of the node
checkId = ChkStart_NodeMsgsAbsDistViolation(NodeToObserve, 30, 2, 40);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
