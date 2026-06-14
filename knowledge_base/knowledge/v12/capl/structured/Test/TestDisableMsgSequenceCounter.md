# TestDisableMsgSequenceCounter

> Category: `Test` | Type: `function`

## Syntax

```c
long TestDisableMsgSequenceCounter (dbMessage aMessage)
```

## Description

Disables the message sequence counter.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// disables the message sequence counter of message ‚MsgToManipulate’ for 2000ms
TestDisableMsgSequenceCounter(MsgToManipulate);
TestWaitForTimeout(2000);
TestEnableMsgSequenceCounter(MsgToManipulate);
```

## Availability

| Since Version |
|---|
