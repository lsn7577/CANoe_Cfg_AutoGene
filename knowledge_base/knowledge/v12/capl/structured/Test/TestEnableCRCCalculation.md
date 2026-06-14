# TestEnableCRCCalculation

> Category: `Test` | Type: `function`

## Syntax

```c
long TestEnableCRCCalculation (dbMessage aMessage);
```

## Description

Re-enables the calculation of the CRC, after it has been disabled with TestDisableCRCCalculation.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// resets the CRC calculation of message ‚MsgToManipulate’ to default behaviour after a break of 2000 ms
TestDisableCRCCalculation(MsgToManipulate);
TestWaitForTimeout(2000);
TestEnableCRCCalculation(MsgToManipulate);
```

## Availability

| Since Version |
|---|
