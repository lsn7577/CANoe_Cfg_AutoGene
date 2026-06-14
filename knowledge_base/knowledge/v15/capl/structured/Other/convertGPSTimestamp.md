# convertGPSTimestamp

> Category: `Other` | Type: `function`

## Syntax

```c
void convertGPSTimestamp(dword timestamp, dword& year, byte& month, byte & day, byte & hour, byte & minute, byte & second);
```

## Description

Converts a GPS time stamp into UTC based date and time information.

## Parameters

| Name | Description |
|---|---|
| timestamp | The GPS time stamp (seconds since 1970-01-01 00:00). |
| year | Receives the year of the time stamp. |
| month | Receives the month of the time stamp (between 1 and 12). |
| day | Receives the day of the time stamp (between 1 and 31). |
| hour | Receives the hour of the time stamp (between 0 and 23). |
| minute | Receives the minute of the time stamp (between 0 and 59). |
| second | Receives the second of the time stamp (between 0 and 59). |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | 13.0 | — | 14 | 1.1 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
