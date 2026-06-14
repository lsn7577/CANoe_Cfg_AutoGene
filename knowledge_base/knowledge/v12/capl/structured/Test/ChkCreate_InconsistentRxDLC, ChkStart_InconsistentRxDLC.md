# ChkCreate_InconsistentRxDLC, ChkStart_InconsistentRxDLC

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_InconsistentRxDLC(Node aNode, char [] aCallback);
```

## Description

Checks the DLC of all Rx messages of a node.

The check condition is violated if the DLC of the message does not agree with the DLC specified in the database.Can only be started in the "on start" area of CAPL or during the measurement. However, the check may be set up as early as in the "pre start" area.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks the DLC of all Rx messages of the node
checkId = ChkStart_InconsistentRxDlc (NodeToObserve);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
