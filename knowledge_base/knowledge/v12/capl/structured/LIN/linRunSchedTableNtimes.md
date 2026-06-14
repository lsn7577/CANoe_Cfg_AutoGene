# linRunSchedTableNtimes

> Category: `LIN` | Type: `function`

## Syntax

```c
long linRunSchedTableNtimes (dword tableIndex, dword numberOfRepetitions, dword onSlotIndex, dword returnToTableIndex);
```

## Description

Switches from the current schedule table to another one, runs the table n times and returns to the initial table or to a different table.

This function only works with LIN core network interfaces.

## Return Values

Index of the current schedule table or -1 if no active schedule table exists and on failure.

## Example

```c
// on pressing key ‘c’ change to schedule table with index 1, run it 2 times and return to the previous table
...
on key 'c'
{
  linRunSchedTableNTimes (1, 2, -2, -1);
}
```

## Availability

| Since Version |
|---|
