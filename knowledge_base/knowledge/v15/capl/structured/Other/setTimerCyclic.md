# setTimerCyclic

> Category: `Other` | Type: `function`

## Syntax

```c
void setTimerCyclic(msTimer t, long firstDuration, long period); // form 1
void setTimerCyclic(msTimer t, long period); // form 2
void setTimerCyclic(timer t, int64 periodInNs); // form 3
```

## Description

Sets a cyclical timer.

With form 2, firstDuration is implicitly the same as period, i.e. the timer runs precisely according to period the first time.

## Parameters

| Name | Description |
|---|---|
| t | The timer to be set. |
| firstDuration | Time in milliseconds until the timer runs out for the first time. |
| period | Time in milliseconds in which the timer is restarted in case of expiration. |
| periodInNs | Time in nanoseconds in which the timer is restarted in case of expiration. |

## Return Values

—

## Example

Starting of a timer that expires the first time 10 ms after the start of measurement and thereafter every 20 ms (10 ms, 30 ms, 50 ms, 70 ms etc.)

```c
variables {
   msTimer t;
}
on start {
   setTimerCyclic(t, 10, 20)
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1: form 1-2 13.0: form 3 | 7.1: form 1-2 13.0: form 3 | 13.0 | 13.0: form 1-2 | 14 | 1.0: form 1-2 5.0: form 3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
