# ILNodeDisturbPduUpdateBit

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeDisturbPduUpdateBit(dbMessage aPDU, long disturbanceCount, long disturbanceValue);
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
  ILNodeDisturbPduUpdateBit("PDU_A", disturbanceCount, updateBit);
}
```

## Availability

| Since Version |
|---|
