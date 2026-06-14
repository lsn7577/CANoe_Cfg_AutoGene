# linChangeSchedtable

> Category: `LIN` | Type: `function`

## Syntax

```c
long linChangeSchedTable(dword tableIndex)
```

## Description

This function switches from the current schedule table to another one.

By calling this function in the event procedure on preStart, it is possible to specify in which schedule table the measurement should start.

## Return Values

Index of the current schedule table or -1 if no active schedule table exists and on failure.

## Example

Change to schedule table with index 1 on pressing 'c' key

```c
...
on key 'c'
{
linChangeSchedTable(1);
}
```

## Availability

| Since Version |
|---|
