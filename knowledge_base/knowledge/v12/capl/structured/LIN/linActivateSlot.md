# linActivateSlot

> Category: `LIN` | Type: `function`

## Syntax

```c
long linActivateSlot(dword tableIndex, dword slotIndex)
```

## Description

Reactivates a schedule table slot defined in the LIN database file (LDF), after having been previously deactivated by linDeactivateSlot().

Schedule slots containing MasterRequests are automatically sent only if their data is updated i.e. using output().

If the Master node is not simulated or no schedule tables are defined, then this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
