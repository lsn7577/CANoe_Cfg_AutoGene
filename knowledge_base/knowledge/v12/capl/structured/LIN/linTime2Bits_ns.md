# linTime2Bits_ns

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linTime2Bits_ns(int64 time)
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
..dword bitTimeSyncBreak;
  bitTimeSyncBreak = linTime2Bits_ns(this.breakLen);
}
```

## Availability

| Since Version |
|---|
