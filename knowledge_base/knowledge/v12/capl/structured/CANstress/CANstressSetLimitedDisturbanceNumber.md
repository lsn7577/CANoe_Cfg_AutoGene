# CANstressSetLimitedDisturbanceNumber

> Category: `CANstress` | Type: `function`

## Syntax

```c
void CANstressSetLimitedDisturbanceNumber (dword cycles, dword distPerCycle, dword cyclePause);
```

## Description

Sets the Limited number of disturbances disturbance mode. In this mode, the number n of disturbances in a disturbance cycle is limited. n disturbances will be followed by a configurable pause p as long as this is not a single disturbance cycle.

## Return Values

—

## Availability

| Since Version |
|---|
