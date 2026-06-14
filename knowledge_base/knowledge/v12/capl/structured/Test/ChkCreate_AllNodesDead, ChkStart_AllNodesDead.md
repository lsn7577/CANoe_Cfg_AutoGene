# ChkCreate_AllNodesDead, ChkStart_AllNodesDead

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_AllNodesDead (Duration aMaxQuietTime, char [] CaplCallback);
```

## Description

All monitored nodes must send at least one of their Tx messages within a specified interval. Otherwise an event will be triggered.

Each node is checked separately, so a dead node is recognized even if others are alive.

Gateway nodes require that the bus context corresponds to the network that is being observed.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks that at least one message is sent in each 100 ms
checkId = ChkStart_AllNodesDead (100);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
