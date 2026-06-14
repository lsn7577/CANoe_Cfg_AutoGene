# ChkCreate_MsgOccurrenceCount, ChkStart_MsgOccurrenceCount

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MsgOccurrenceCount(dbMessage aMessage, long aMaxCount);
```

## Description

Checks the absence of the specified message on the bus. An event is created if more than aMaxCount of the specified message were sent.

The numeric functions/constructors with the parameter 'aMessageId/aSourceAdr' cannot be used for FlexRay. Instead use the numeric constructors with the parameter 'slotID' (that can only be applied to a FlexRay bus).

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks that the message is sent less than 3 times
checkId = ChkStart_MsgOccurrenceCount (MsgToObserve, 2);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
