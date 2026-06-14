# linGetDominantTimeout

> Category: `LIN` | Type: `function`

## Syntax

```c
int64 linGetDominantTimeout();
```

## Description

Returns the dominant timeout of the current channel’s transceiver in nanoseconds. If zero, the transceiver does not have any dominant timeout.

## Return Values

Returns the dominant timeout of the LINcab/LINpiggy or zero, if the transceiver does not have any dominant timeout.

## Availability

| Since Version |
|---|
