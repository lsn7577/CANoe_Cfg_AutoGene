# OnMostSystemLock

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostSystemLock(long oldstate, long newstate)
```

## Description

This event procedure is called each time the state of the System-Lock flag changes.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

## Return Values

1: System Lock Flag set.
0: System Lock Flag not set.

## Availability

| Since Version |
|---|
