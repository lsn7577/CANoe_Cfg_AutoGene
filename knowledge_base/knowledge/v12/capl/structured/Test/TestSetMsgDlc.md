# TestSetMsgDlc

> Category: `Test` | Type: `function`

## Syntax

```c
long TestSetMsgDlc (dbMessage aMessage, dword dlc);
```

## Description

Assigns a new DLC to the message.

For CAN FD in this function the DLC must be set.

For the values 0-8, DLC and data length is the same value.

For the values 9-12, DLC and data length differ:

This function influences a simulation node with an assigned CANoe Interaction Layer.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// set the DLC of message ‘MsgToManipulate’ for 2000 ms to a specified length
TestSetMsgDLC(MsgToManipulate, 4);
TestWaitForTimeout(2000);
TestResetMsgDLC(MsgToManipulate);
```

## Availability

| Since Version |
|---|
