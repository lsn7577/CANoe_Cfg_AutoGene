# linTime2Bits

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword linTime2Bits(dword time)
```

## Description

This function converts specified system times to bit times. The conversion is done using the current baud rate on the channel determined by the CAPL program context.

Calling this function with the explicit channel is only possible from a CAPL program defined in the Measurement Setup of CANoe.

## Return Values

Resulting bit time.

## Example

Extract sync break length of LIN frames

```c
on linFrame *
{
dword sysTimeSyncBreak; // time in 10µs units
dword bitTimeSyncBreak; // time in bit time units
sysTimeSyncBreak = linGetSyncBreakLength(this);
bitTimeSyncBreak = linTime2Bits(sysTimeSyncBreak);
}
```

## Availability

| Since Version |
|---|
