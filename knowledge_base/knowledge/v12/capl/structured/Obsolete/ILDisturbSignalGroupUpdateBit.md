# ILDisturbSignalGroupUpdateBit

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long ILDisturbSignalGroupUpdateBit(dbMessage aMessage, char aSigGroupName[], long disturbanceMode, long disturbanceCount, long disturbanceValue);
```

## Description

Modifies the update bit of a signal group. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer

## Return Values

0: No error

## Example

```c
// Sets the Signal Group Update Bit to 0

variables {
  long disturbanceMode  = 0; // The disturbance uses the value in disturbanceValue as Update Bit.
  int disturbanceCount  = 100;
  long disturbanceValue = 0;
}

on key 'a'{
  ILDisturbSignalGroupUpdateBit(Message_A, "SignalGroup_A", disturbanceMode, disturbanceCount, disturbanceValue);
}
```

## Availability

| Up to Version |
|---|
