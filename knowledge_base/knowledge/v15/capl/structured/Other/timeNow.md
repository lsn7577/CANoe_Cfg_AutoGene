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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
