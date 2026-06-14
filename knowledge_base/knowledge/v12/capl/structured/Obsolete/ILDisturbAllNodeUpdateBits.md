# ILDisturbAllNodeUpdateBits

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long ILDisturbAllNodeUpdateBits (long flags, long disturbanceMode, long disturbanceCount, long disturbanceValue);
```

## Description

Modifies all update bits of signals/signal groups of all nodes in the current bus context. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer.

## Parameters

| Name | Description |
|---|---|
| 0 | Update bits of signals and signal groups are disturbed. |
| 1 | Only signal update bits are disturbed. |
| 2 | Only signal group update bits are disturbed. |

## Return Values

0: No error

## Availability

| Up to Version |
|---|
