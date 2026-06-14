# timeNow

> Category: `Other` | Type: `function`

## Syntax

```c
dword timeNow();
```

## Description

Supplies the current simulation time (maximum time: .2^32 * 10 microseconds = 11 hours, 55 minutes, 49 seconds, 672 milliseconds, 96 microseconds)

The simulation time can be correlated with the hardware results of the interface cards (e.g. CANcardXL).The resolution of this time is dependent upon the hardware used (usually a millisecond or better).

Depending on the hardware configuration, the simulation time

or

## Return Values

Simulation time in 10 microseconds.

## Example

```c
...
float x;
x = timeNow()/100000.0; //current time in seconds
...
```

## Availability

| Since Version |
|---|
