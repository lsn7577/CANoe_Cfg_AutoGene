# addTimeToMeasurementStartTime

> Category: `Other` | Type: `function`

## Syntax

```c
long addTimeMeasurementStartTime(int64 timeSpan, long time[]);
```

## Description

Calculates the absolute date/time of the measurement start plus an offset (e.g. a timestamp).

## Parameters

| Name | Description |
|---|---|
| timeSpan | Time to be added to the measurement start time, e.g. a timestamp of a measured frame. |
| Index | Information |
| 0 | Milliseconds (0 - 999) |
| 1 | Seconds (0 - 59) |
| 2 | Minutes (0 - 59) |
| 3 | Hours (0 - 23) |
| 4 | Day of month (1 - 31) |
| 5 | Month (0 - 11) |
| 6 | Year (0 - xxx, offset of 1900, e.g. 117 = 2017) |
| 7 | Day of week (0 - 6, Sunday is 0) |

## Return Values

1 if successful, 0 if not (e.g. array to small).

## Example

```c
on errorframe
{
  long time[8];
  addTimeToMeasurementStartTime(timeNowNS(), time);
  write("ErrorFrame occured on %02d/%02d/%02d %02d:%02d:%02d.%-3d",
  time[5]+1, time[4], time[6]-100, time[3], time[2], time[1], time[0]);
  getMeasurementStartTime(time);
  write("Measurement was started on %02d/%02d/%02d %02d:%02d:%02d.%-3d",
  time[5]+1, time[4], time[6]-100, time[3], time[2], time[1], time[0]);
}

// Output e.g.:
// ErrorFrame occured on 08/15/17 14:39:46.787
// Measurement was started on 08/15/17 14:39:29.547
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 SP3 | 10.0 SP3 | 13.0 | — | 14 | 2.2 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
