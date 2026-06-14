# getMeasurementStartTime

> Category: `Other` | Type: `function`

## Syntax

```c
long getMeasurementStartTime(long time[]);
```

## Description

Returns details about the absolute time the measurement was started.

## Parameters

| Name | Description |
|---|---|
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
