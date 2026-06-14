# ILNodeDisturbSignalUpdateBit

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeDisturbSignalUpdateBit(dbSignal aSignal, long disturbanceMode, long disturbanceCount, long disturbanceValue);
```

## Description

This function modifies the update bit of a signal. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer.

## Return Values

0: No error

## Example

```c
// Sets the Signal Update Bit to 0

variables {
  long disturbanceMode  = 0; // The disturbance uses the value in disturbanceValue as Update Bit.
  int disturbanceCount  = 100;
  long disturbanceValue = 0;
}

on key 'a'{
  ILNodeDisturbSignalUpdateBit("PDU_A", "Signal_A", disturbanceMode, disturbanceCount, disturbanceValue);
}
```

## Availability

| Since Version |
|---|
