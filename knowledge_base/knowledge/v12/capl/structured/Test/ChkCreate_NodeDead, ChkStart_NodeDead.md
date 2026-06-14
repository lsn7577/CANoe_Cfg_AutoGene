# ChkCreate_NodeDead, ChkStart_NodeDead

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_NodeDead (Node n, Duration aMaxQuietTime, char [] CaplCallback); // form 1
```

## Description

All monitored nodes must send at least one of their Tx messages within a specified interval. Otherwise an event will be triggered.

Gateway nodes require that the bus context corresponds to the bus that is being observed. This means that the check only works correctly if the current bus context corresponds to the database in which the node is defined.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks that at least one message of the node is sent in each 100 ms
checkId = ChkStart_NodeDead (100);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
