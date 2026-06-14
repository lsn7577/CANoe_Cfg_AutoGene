# ILDisturbSignalUpdateBit

> Category: `Obsolete` | Type: `function`

## Syntax

```c
ILDisturbSignalUpdateBit("PDU_A", "Signal_A", disturbanceMode, disturbanceCount, disturbanceValue);
```

## Description

This function modifies the update bit of a signal. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer.

## Parameters

| Name | Description |
|---|---|
| aPDUName | Name of the PDU that should be modified. |

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
  ILDisturbSignalUpdateBit("PDU_A", "Signal_A", disturbanceMode, disturbanceCount, disturbanceValue);
}
```

## Availability

| Up to Version |
|---|
