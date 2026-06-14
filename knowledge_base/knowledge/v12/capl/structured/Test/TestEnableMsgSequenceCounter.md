# TestEnableMsgSequenceCounter

> Category: `Test` | Type: `function`

## Syntax

```c
long TestEnableMsgSequenceCounter (dbMessage aMessage);
```

## Description

Re-enables the message sequence counter, after it has been disabled with TestDisableMsgSequenceCounter.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// disables the message sequence counter of message ‚MsgToManipulate’ for 2000ms
// and re-enables the message sequence counter afterwards
TestDisableMsgSequenceCounter(MsgToManipulate);
TestWaitForTimeout(2000);
TestEnableMsgSequenceCounter(MsgToManipulate);
```

## Availability

| Since Version |
|---|
