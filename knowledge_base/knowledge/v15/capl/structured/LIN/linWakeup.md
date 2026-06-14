# linWakeup

> Category: `LIN` | Type: `function`

## Syntax

```c
long linWakeup(); // form 1
linWakeup(dword ttobrk, dword wakeupSignalCount, dword widthInMicSec); // from 2
```

## Description

Sends wakeup signals. Wakeup signals can only be sent while the LIN hardware is in Sleep mode. If no parameters are given, the default parameters or the parameters configured with linSetWakeupTimings are used. Wake up timings can be configured per node for nodes defined in a LIN database. If no database is used the signature using wake parameters shall be used.

## Parameters

| Name | Description |
|---|---|
| ttobrk | This parameter specifies the time difference between the transmissions of two consecutive Wakeup frames, i.e. the time between end of one wakeup frame and start of the next one. Units of this parameter as well as default value depend on the hardware settings (see Hardware Configuration: LIN). Value range (for units expected in bit times): 20..50000 Value range (for units expected in ms): 1..65536 |
| wakeupSignalCount | Sets the number of Wakeup frame retransmissions. Value range: 1…255 Default value depends on the hardware settings (see Hardware Configuration: LIN). |
| widthInMicSec | This parameter sets the width of the wakeup frame to be sent in microseconds. The resolution is 50 µs. This parameter is only used by slave nodes applying LIN protocol starting with version 2.0. Value range: 250..5000 µs Default value depends on the hardware settings (see Hardware Configuration: LIN). |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// send a wakeup signal via a keyboard event
on key 'w'
{
  linWakeup();
}
// send wakeup signal 3 times with 150 ms delay between 2 consecutive signals and a length of 300 us
linWakeup(150, 3, 300);
...
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | 13.0 | 13.0 | — | 2.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
