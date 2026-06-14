# linBits2Time

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword linBits2Time(dword bitTimes)
```

## Description

Converts specified bit time to an absolute time.

The absolute time is calculated using the current baud rate on the channel determined by the CAPL program context.

## Return Values

Absolute time in 10 µs.

## Example

Convert header bit time of a LIN frame to µs

```c
on linFrame *
{
dword headerTimeInMicroSeconds; // time in µs
headerTimeInMicroSeconds = linBits2Time(this.LIN_HeaderTime)*10;
}
```

## Availability

| Since Version |
|---|
