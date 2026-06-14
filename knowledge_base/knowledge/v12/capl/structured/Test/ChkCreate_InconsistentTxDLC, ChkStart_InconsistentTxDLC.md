# ChkCreate_InconsistentTxDLC, ChkStart_InconsistentTxDLC

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_InconsistentTxDLC(Node aNode, char [] aCallback);
```

## Description

Checks the DLC of all Tx messages of a node.

The check condition is violated if the DLC of the message does not agree with the DLC specified in the database.Can only be started in the "on start" area of CAPL or during the measurement. However, the check may be set up as early as in the "pre start" area.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: Check could not be created and may not be referenced.

## Example

```c
// checks the DLC of all Tx messages of the node
checkId = ChkStart_InconsistentTxDlc (NodeToObserve);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
