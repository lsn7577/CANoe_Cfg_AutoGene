# TestResetMsgDlc

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetMsgDlc (dbMessage aMessage);
```

## Description

Resets the DLC to the DLC of the database.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// reset the DLC of message ‘MsgToManipulate’
TestSetMsgDLC(MsgToManipulate, 4);
TestWaitForTimeout(2000);
TestResetMsgDLC(MsgToManipulate);
```

## Availability

| Since Version |
|---|
