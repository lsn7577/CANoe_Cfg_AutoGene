# canGetChipState

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long canGetChipState (long channel)
```

## Description

Returns the current chip state of the specified CAN controller.

## Return Values

Chip state of the specified CAN controller. See the following table for a description of the return values.
0
Value not available
1
Simulated
3
Error Active
4
Warning Level
5
Error Passive
6
Bus Off

## Availability

| Up to Version |
|---|
