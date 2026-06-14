# linSetWakeupTimings

> Category: `LIN` | Type: `function`

## Syntax

```c
linSetWakeupTimings(long ttobrk, long wakeupSignalcount, dword widthInMicSec);
```

## Description

Configures wake-up timings. Wake-up timings can be configured per node for nodes defined in a LIN database.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// Configures the wake up timings for the database node "LINMaster".
linSetWakeupTimings(150, 3, 250, “LINMaster”)

// send a wakeup signal via a keyboard event within the CAPL programe of the node 
// "LINMaster". The configured timings will be used.
on key 'w'
{
  linWakeup();
}
```

## Availability

| Since Version |
|---|
