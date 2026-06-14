# ILDisturbPduUpdateBit

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long ILDisturbPduUpdateBit(char aPduName[], int disturbanceCount, int updateBit);
```

## Description

This function modifies the update bit of a PDU. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer.

## Return Values

0: No error

## Example

```c
// Sets the PDU Update Bit 100 times to 0

variables {
  int disturbanceCount = 100;
  int updateBit = 0;
}

on key 'a'{
  ILDisturbPduUpdateBit("PDU_A", disturbanceCount, updateBit);
}
```

## Availability

| Up to Version |
|---|
