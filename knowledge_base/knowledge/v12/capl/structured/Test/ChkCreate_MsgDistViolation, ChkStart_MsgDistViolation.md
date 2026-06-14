# ChkCreate_MsgDistViolation, ChkStart_MsgDistViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MsgDistViolation (Message aReferenceMessage, Message aObservedMessage, duration aMinDistance, duration aMaxDistance, Callback aCallback);
```

## Description

Event is generated if the time interval that starts on receipt of the reference message and ends with the receipt of the observed message is smaller than aMinDistance or is larger than aMaxDistance.

The numeric constructors with the parameter 'slotID1/2' can only be applied to a FlexRay bus.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks the distance between two messages
checkId = ChkStart_MsgDistViolation (ReferenceMsg, MsgToObserve, 90, 110);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
