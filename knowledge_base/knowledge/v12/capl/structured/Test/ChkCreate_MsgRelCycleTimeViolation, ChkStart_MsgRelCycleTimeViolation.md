# ChkCreate_MsgRelCycleTimeViolation, ChkStart_MsgRelCycleTimeViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MsgRelCycleTimeViolation (Message aObservedMessage, double aMinRelCycleTime, double aMaxRelCycleTime, Callback aCallback);
```

## Description

Checks the occurrences of cyclic messages.

Event is generated if the time between sends of the message is smaller than minRelCycleTime * GenMsgCycleTime (DB-attribute) or larger than maxRelCycleTime * GenMsgCycleTime.

Not to be checked limits are set to 0; there must be at least one limit specified.

Can be started only in the 'on start' section of CAPL or during measurement.

The numeric constructors with the parameter 'slotID' can only be applied to a FlexRay bus.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks the cycle time of the message
checkId = ChkStart_MsgRelCycleTimeViolation (MsgToObserve, 0.9, 1.1);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
