# setTimer

> Category: `Other` | Type: `function`

## Syntax

```c
void setTimer(msTimer t, long duration); // form 1
void setTimer(timer t, long duration); // form 2
void setTimer(timer t, long durationSec, long durationNanoSec); // form 3
```

## Description

Sets a timer.

## Return Values

—

## Example

```c
variables {
  msTimer t1;
  Timer t23;
}

on key F1 {
  setTimer(t1, 200); // set timer t1 to 200 ms
}

on key F2 {
  setTimer (t23, 2); // set timer t23 to 2 sec
}

on key F3 {
  setTimer (t23, 0, 1250*1000 ); // set timer t23 to 1.250 milliseconds
}

on timer t1 {
  write("F1 was pressed 200ms ago");
}

on timer t23 {
  write("F2 was pressed 2 sec ago or F3 1250000 nsec ago");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All 7.0 SP5: methods | All 7.0 SP5: methods | 13.0 | 13.0: form 1-2 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
