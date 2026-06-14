# linSetWakeupTimings

> Category: `LIN` | Type: `function`

## Syntax

```c
linSetWakeupTimings(long ttobrk, long wakeupSignalcount, dword widthInMicSec); // form 1
linSetWakeupTimings(long ttobrk, long wakeupSignalcount, dword widthInMicSec, char nodeName[]); // form 2
```

## Description

Configures wake-up timings. Wake-up timings can be configured per node for nodes defined in a LIN database.

## Parameters

| Name | Description |
|---|---|
| ttobrk | This parameter specifies the time difference between the transmissions of two consecutive Wakeup frames, i.e. the time between end of one wakeup frame and start of the next one. Units of this parameter as well as default value depend on the hardware settings (see Hardware Configuration: LIN). Value range (for units expected in bit times): 20..50000 Value range (for units expected in ms): 1..65536 |
| wakeupSignalCount | Sets the number of Wakeup frame retransmissions. Value range: 1..255 Default value depends on the hardware settings (see Hardware Configuration: LIN). |
| widthInMicSec | This parameter sets the width of the wakeup frame to be sent in microseconds. The resolution is 50 µs. This parameter is only used by LIN2.0 slave nodes. Value range: 250..5000 µs Default value depends on the hardware settings (see Hardware Configuration: LIN). |
| nodeName | Name of a LIN node defined in the database. |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// Configures the wake up timings for the database node "LINMaster".
linSetWakeupTimings(150, 3, 250, “LINMaster”)

// send a wakeup signal via a keyboard event within the CAPL programe of the node 
// "LINMaster". The configured timings will be used.
on key 'w'
{
  linWakeup();
}
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
