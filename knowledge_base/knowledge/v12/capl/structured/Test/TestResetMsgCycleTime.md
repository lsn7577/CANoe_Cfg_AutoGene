# TestResetMsgCycleTime

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetMsgCycleTime (dbMessage aMessage);
```

## Description

Resets the cycle time of the message to the database cycle time, after having changed it with TestSetMsgCycleTime(...).

This function influences a simulation node with an assigned CANoe Interaction Layer.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// reset the cycle time of message ‘MsgToManipulate’
TestSetMsgCycleTime(MsgToManipulate, 200);
TestWaitForTimeout(2000);
TestResetMsgCycleTime(MsgToManipulate);
```

## Availability

| Since Version |
|---|
