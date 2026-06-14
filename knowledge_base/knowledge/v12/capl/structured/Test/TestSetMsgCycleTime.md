# TestSetMsgCycleTime

> Category: `Test` | Type: `function`

## Syntax

```c
long TestSetMsgCycleTime(dbMessage aMessage, float aNewCycleTime);
```

## Description

Assigns a new cycle time to the message.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error

## Example

```c
// set the cycle time of message ‘MsgToManipulate’ to a specified value for 2000 ms
TestSetMsgCycleTime(MsgToManipulate, 200);
TestWaitForTimeout(2000);
TestResetMsgCycleTime(MsgToManipulate);
```

## Availability

| Since Version |
|---|
