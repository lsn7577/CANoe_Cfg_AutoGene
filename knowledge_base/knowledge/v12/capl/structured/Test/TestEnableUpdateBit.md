# TestEnableUpdateBit

> Category: `Test` | Type: `function`

## Syntax

```c
long TestEnableUpdateBit (dbSignal aSignal);
```

## Description

Re-enables the standard behaviour of the update bit, after it has been disabled with TestDisableUpdateBit.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// disables the update bit of signal ‘DoorStatus_UB’ for 1000 ms
TestDisableUpdateBit(DoorStatus_UB, 0);
TestWaitForTimeout(1000);
TestEnableUpdateBit(DoorStatus_UB);
```

## Availability

| Since Version |
|---|
