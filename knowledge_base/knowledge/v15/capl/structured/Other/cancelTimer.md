# cancelTimer

> Category: `Other` | Type: `function`

## Syntax

```c
void cancelTimer(msTimer t); // from 1
void cancelTimer(timer t); // from 2
```

## Description

Stops an active timer.

## Return Values

—

## Example

```c
variables {
msTimer takt;
message 100 data = {dlc = 1, byte(0) = 0xFF, dir = Tx};
}
on Timer takt{
output(data);
setTimer(takt, 200);
}
on key F1 {
cancelTimer(takt); // cancel timer
write("canceled");
}
on key F2 {
setTimer(takt, 200); // set timer to 200ms
write("start");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All 7.0 SP5: method | All 7.0 SP5: method | 13.0 | 13.0: form 1 | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
