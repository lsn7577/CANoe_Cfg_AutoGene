# ChkCreate_PayloadGapsObservationTx, ChkStart_PayloadGapsObservationTx

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_PayloadGapsObservationTx(Node aNode, long defaultBitValue, char [] aCallback);
```

## Description

Checks the payload gaps and the DLC of all Tx messages of a node.

The check condition is violated if the payload gaps do not match the specified default bit value or the DLC does not match the specified DLC of the database.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks the payload gaps of the message
checkId = ChkStart_PayloadGapsObservationTx(NodeToObserve, 0);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
