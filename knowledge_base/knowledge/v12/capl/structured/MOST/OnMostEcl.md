# OnMostEcl

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostEcl(long eclState)
```

## Description

The event procedure is called when the state of the Electrical Control Line has changed.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

## Return Values

—

## Example

Output of ECL changes with time stamp.

```c
OnMostEcl(long eclState)
{
   write(„ECL state at %fs: %d“, mostEventTimeNs() / 1.0e9, eclState);
}
```

## Availability

| Since Version |
|---|
