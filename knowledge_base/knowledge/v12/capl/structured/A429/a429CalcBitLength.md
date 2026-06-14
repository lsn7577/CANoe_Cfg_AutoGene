# a429CalcBitLength

> Category: `A429` | Type: `function`

## Syntax

```c
dword a429CalcBitLength( long channel, dword BitTimes );
```

## Description

For every channel there is a relation between a bit time and the length of a bit time. This relation is determined by the channel bit rate. In order to make it easier to provide the gap length a429SetGap in bit times this function converts these values for a given channel.

## Availability

| Since Version |
|---|
