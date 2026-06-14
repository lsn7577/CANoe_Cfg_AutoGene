# TestDisableMsgAllTx

> Category: `Test` | Type: `function`

## Syntax

```c
long TestDisableMsgAllTx (char [] aNode)
```

## Description

Disables the sending of all tx messages of the node except the sending with testSetMsgEvent.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// send a message event for a message which is disabled by TestDisableMsgAllTx
TestDisableMsgAllTx(NodeToManipulate);
TestWaitForTimeout(5000);
TestSetMsgEvent(MsgToManipulate);
TestWaitForTimeout(5000);
TestEnableMsgAllTx(NodeToManipulate);
```

## Availability

| Since Version |
|---|
