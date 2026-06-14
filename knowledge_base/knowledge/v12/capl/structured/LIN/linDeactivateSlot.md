# linDeactivateSlot

> Category: `LIN` | Type: `function`

## Syntax

```c
long linDeactivateSlot(dword tableIndex, dword slotIndex)
```

## Description

This function deactivates the specified slot of schedule table. For example, it can be used to turn slots off in a diagnostic table.

By calling this function in the event procedure on preStart, it is possible to configure initial state of schedule table.

If the Master node is not simulated or no schedule tables are defined, then this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
