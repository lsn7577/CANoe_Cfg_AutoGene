# ChkCreate_InconsistentDLC, ChkStart_InconsistentDLC

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_InconsistentDLC(Message aMessage, char [] aCallback);
```

## Description

Checks the DLC, respectively the payload length of a message.

The check condition is violated if the DLC of the message does not agree with the specified DLC of the database.Can only be started in the "on start" area of CAPL or during the measurement. However, the check may be set up as early as in the "pre start" area.

The numeric functions/constructors with the parameter 'aMessageId' cannot be used for FlexRay. Instead use the numeric constructors with the parameter 'slotID' (that can only be applied to a FlexRay bus).

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks the DLC of the message
checkId = ChkStart_InconsistentDlc (MsgToObserve);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
