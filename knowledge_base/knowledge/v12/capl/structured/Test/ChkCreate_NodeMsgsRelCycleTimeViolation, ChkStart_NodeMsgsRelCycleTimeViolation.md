# ChkCreate_NodeMsgsRelCycleTimeViolation, ChkStart_NodeMsgsRelCycleTimeViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_NodeMsgsRelCycleTimeViolation (Node aNode, double aMinRelCycleTime, double aMaxRelCycleTime, Callback aCallback);
```

## Description

Checks the occurrences of cyclic messages of the given send node.

Event is generated if the time between sends of the (same) message is smaller than minRelCycleTime * GenMsgCycleTime (DB-attribute) or larger than maxRelCycleTime * GenMsgCycleTime.

Not to be checked limits are set to 0; there must be at least on limit specified.

Not checked are send messages with a specified cycle time equal to 0 or network management messages or diagnostic messages.

Can be started only in the start-section of CAPL or during measurement.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks the cycle time of all messages of the node
checkId = ChkStart_NodeMsgsRelCycleTimeViolation (NodeToObserve, 0.9, 1.1);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
