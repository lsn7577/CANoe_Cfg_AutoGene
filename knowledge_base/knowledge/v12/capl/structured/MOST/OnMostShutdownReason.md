# OnMostShutdownReason

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostShutdownReason(long oldReason, long newReason)
```

## Description

This event procedure is called each time when the shutdown reason changes.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

The following reason values are defined based on the MOST Specification 3.0:

0

No result available

1

No fault saved

2

Failure ‘Sudden Signal Off’

3

Failure ‘Critical Unlock’

## Return Values

—

## Availability

| Since Version |
|---|
