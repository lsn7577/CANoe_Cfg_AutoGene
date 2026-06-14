# timeToElapse

> Category: `Other` | Type: `function`

## Syntax

```c
long timeToElapse(timer t); // from 1
long timeToElapse(mstimer t); // from 2
```

## Description

Returns a value indicating how much more time will elapse before an on timer event procedure is called.

For form 1, the time value is returned in seconds; for form 2, the time value is returned in milliseconds.

If the timer is not active, -1 is returned. This is also the case in the on timer event procedure itself.

## Return Values

Time to go until the timer elapses and the event procedure is called.

## Example

```c
timer t;
setTimer(t, 5);
write("Time to elapse: %d", timeToElapse(t)); // writes 5
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
