# TestDisableMsg

> Category: `Test` | Type: `function`

## Syntax

```c
long TestDisableMsg (dbMessage aMessage);
```

## Description

Disables the sending of the message except by calling the function TestSetMsgEvent. Use TestEnableMsg to re-enable the message.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// send a message event for the disabled message ‘MsgToManipulate’
TestDisableMsg(MsgToManipulate);
TestWaitForTimeout(5000);
TestSetMsgEvent(MsgToManipulate);
TestWaitForTimeout(5000);
TestEnableMsg(MsgToManipulate);
```

## Availability

| Since Version |
|---|
