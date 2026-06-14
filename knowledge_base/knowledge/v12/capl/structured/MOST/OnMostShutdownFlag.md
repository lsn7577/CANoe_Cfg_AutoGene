# OnMostShutdownFlag

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostShutdownFlag(long oldstate, long newstate)
```

## Description

This event procedure is called each time the state of the Shutdown flag changes.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

## Return Values

1: Shutdown Flag set.

## Availability

| Since Version |
|---|
