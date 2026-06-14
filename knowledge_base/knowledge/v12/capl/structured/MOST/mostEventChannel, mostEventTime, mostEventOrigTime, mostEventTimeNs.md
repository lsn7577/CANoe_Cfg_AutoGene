# mostEventChannel, mostEventTime, mostEventOrigTime, mostEventTimeNs

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostEventChannel()
```

## Description

long mostEventChannel() returns the channel over which the event arrived.

dword mostEventTime() returns the time stamp of the event (Units: 10 µs).

dword mostEventOrigTime() returns the hardware-generated time stamp of the event (Units: 10 µs).

float mostEventTimeNs() returns the time stamp of the event (Units: 1 ns).

## Return Values

Time stamp

## Example

```c
OnMostNodeAdr(long nodeadr)
{
   write("Node address changed to %04X on channel %d at %fs",
      nodeadr,
      mostEventChannel(),
      mostEventTime() / 100000.0);
}
```

## Availability

| Since Version |
|---|
