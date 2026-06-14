# ILNodeDisturbChecksum

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeDisturbChecksum(dbMessage aMessage, char aSigGroupName[], long checksumType, long disturbanceMode, long disturbanceCount, long disturbanceValue); // form 1
```

## Description

This function modifies the checksum. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer.

## Return Values

0: No error

## Example

```c
// Disturbs the Checksum of a specific PDU, disturbance pattern: 20x fix value

variables {
  long checksumType = 0; // The possible values are described in the corresponding OEM Package manual.
  long disturbanceMode = 0; // The disturbance uses the value in disturbanceValue as checksum.
  long disturbanceCount = 20;
  long disturbanceValue = 10;
}

on key 'a' {
  ILNodeDisturbChecksum("PDU_A", "", checksumType, disturbanceMode, disturbanceCount, disturbanceValue);
}
```

## Availability

| Since Version |
|---|
