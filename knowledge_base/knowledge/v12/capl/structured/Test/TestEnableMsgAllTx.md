# TestEnableMsgAllTx

> Category: `Test` | Type: `function`

## Syntax

```c
long TestEnableMsgAllTx (char [] aNode);
```

## Description

Re-enables the sending of all tx messages of the node after having disabled it with TestDisableMsgAllTx.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// send a message event for a message which is disabled by TestDisableMsgAllTx
// and re-enable the sending of all tx messages of node ‚NodeToManipulate’
TestDisableMsgAllTx(NodeToManipulate);
TestWaitForTimeout(5000);
TestSetMsgEvent(MsgToManipulate);
TestWaitForTimeout(5000);
TestEnableMsgAllTx(NodeToManipulate);
```

## Availability

| Since Version |
|---|
