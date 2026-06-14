# OnMostEclSequence

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostEclSequence(long state)
```

## Description

The event procedure is called before the beginning and after the end of a sequence on the Electrical Control Line.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

## Return Values

—

## Example

Output of ECL sequence changes with time stamp.

```c
OnMostEclSequence(long state)
{
   if(state == 0)
      write(„ECL sequence stopped at %fs“, MostEventTimeNs() / 1.0e9);
   else
      write(„ECL sequence started at %fs“, MostEventTimeNs() / 1.0e9);
}
```

## Availability

| Since Version |
|---|
