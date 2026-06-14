# ChipState

> Category: `CAN` | Type: `function`

## Syntax

```c
long ChipState ()
CANx.ChipState
```

## Description

Returns the current chip state of the CAN x controller.

Valid x values: 1…32

## Return Values

Chip state of the CAN x controller. See the following table for a description of the return values.
0
Value not available
1
Simulated
2
Not used
3
Error Active
4
Warning Level
5
Error Passive
6
Bus Off
A description of the chip states can also be found here: Bus Statistics Window of option CAN.

## Example

```c
write ("Chip state of CAN1 = %d", CAN1.ChipState);
```

## Availability

| Since Version |
|---|
