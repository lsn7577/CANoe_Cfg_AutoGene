# linBits2Time_ns

> Category: `LIN` | Type: `function`

## Syntax

```c
int64 linBits2Time_ns(dword bitTimes)
```

## Description

Converts specified bit time to an absolute time.

The absolute time is calculated using the current baud rate on the channel determined by the CAPL program context.

## Return Values

Absolute time in ns.

## Example

Convert header bit time of a LIN frame to ns

```c
on linFrame *
{
int64 headerTimeInNanoSeconds; // time in ns
headerTimeInNanoSeconds = linBits2Time_ns(this.LIN_HeaderTime);
}
```

## Availability

| Since Version |
|---|
