# timeNowNS, timeNowInt64

> Category: `Other` | Type: `function`

## Syntax

```c
float TimeNowNS();
```

## Description

Supplies the current simulation time.

The simulation time can be correlated with the hardware results of the interface cards (e.g. CANcardXL).The resolution of this time is dependent upon the hardware used (usually a millisecond or better).

Depending on the hardware configuration, the simulation time

or

## Return Values

Simulation time in nanoseconds.

## Availability

| Since Version |
|---|
