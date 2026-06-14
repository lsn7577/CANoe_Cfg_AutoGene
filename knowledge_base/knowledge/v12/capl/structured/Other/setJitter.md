# setJitter

> Category: `Other` | Type: `function`

## Syntax

```c
setJitter(int min, int max)
```

## Description

The Jitter interval for the timers of a network node can be set with this function. The two values may lie between –10000 and 10000 (corresponds to –100.00% to 100.00%). If one of the two values does not lie within this range, a message is output in the Write Window.

Setting of a Jitter will cause any existing Drift to be reset. To utilize Jitter and Drift simultaneously please refer to the example.

## Return Values

—

## Example

```c
...
// Set a Jitter with +–4 percent
setJitter(-400, 400);
...
...
// Set a Jitter with +–4 percent
// and a Drift of 17 percent
setJitter(1300, 2100);
...
```

## Availability

| Since Version |
|---|
