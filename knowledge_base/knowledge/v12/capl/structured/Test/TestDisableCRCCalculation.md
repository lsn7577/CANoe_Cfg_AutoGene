# TestDisableCRCCalculation

> Category: `Test` | Type: `function`

## Syntax

```c
long TestDisableCRCCalculation (dbMessage aMessage);
```

## Description

Disables the calculation of the CRC of a message.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// disables the CRC calculation of message ‚MsgToManipulate’ for 2000 ms
TestDisableCRCCalculation(MsgToManipulate);
TestWaitForTimeout(2000);
TestEnableCRCCalculation(MsgToManipulate);
```

## Availability

| Since Version |
|---|
