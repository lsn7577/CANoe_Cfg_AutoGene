# setDrift

> Category: `Other` | Type: `function`

## Syntax

```c
void setDrift(int drift)
```

## Description

A constant deviation can be set for the timers of a network node with this function. Inputs for the two values may lie between –10000 and 10000 (corresponds to –100.00% to 100.00%). If the value does not lie within this range, a message is output in the Write Window.

Setting of a Drift causes any existing Jitter to be reset.

## Return Values

—

## Example

```c
...
// Sets the Drift to 35.5 percent
setDrift(3550);
...
```

## Availability

| Since Version |
|---|
