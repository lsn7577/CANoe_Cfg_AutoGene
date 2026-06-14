# ChkCreate_PayloadGapsObservation, ChkStart_PayloadGapsObservation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_PayloadGapsObservation(Message aMessage, long defaultBitValue, char [] aCallback);
```

## Description

Checks the payload gaps and the DLC of a message.

The check condition is violated if the payload gaps do not match the specified default bit value or the DLC does not match the specified DLC of the database.

The numeric functions/constructors with the parameter aMessageId cannot be used for FlexRay. Instead use the numeric constructors with the parameter slotID (that can only be applied to a FlexRay bus).

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous Frames are ignored.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks the payload gaps of the message
checkId = ChkStart_PayloadGapsObservation(MsgToObserve, 0);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
