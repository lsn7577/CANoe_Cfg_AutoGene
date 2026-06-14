# ILNodeDisturbSignalGroupUpdateBit

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeDisturbSignalGroupUpdateBit(dbMessage aMessage, char aSigGroupName[], long disturbanceMode, long disturbanceCount, long disturbanceValue); // form 1
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
  ILNodeDisturbSignalGroupUpdateBit(Message_A, "SignalGroup_A", disturbanceMode, disturbanceCount, disturbanceValue);
}
```

## Availability

| Since Version |
|---|
