# convertTimestamp, convertTimestampNS

> Category: `Other` | Type: `function`

## Syntax

```c
void convertTimestamp(dword timestamp, dword& days, byte& hours, byte& minutes, byte& seconds, word& milliSeconds, word& microSeconds); // form 1
void convertTimestampNS(qword timestamp, dword& days, byte& hours, byte& minutes, byte& seconds, word& milliSeconds, word& microSeconds, word& nanoSeconds); // form 2
```

## Description

Converts a time stamp to separate parts

(form 1: maximum time: .2^32 * 10 microseconds = 11 hours, 55 minutes, 49 seconds, 672 milliseconds, 96 microseconds).

## Parameters

| Name | Description |
|---|---|
| timestamp | time stamp in 10 microseconds (form 1) time stamp in nanoseconds (form 2) |
| days | Receives the days of the time stamp |
| hours | Receives the hours the time stamp (between 0 and 23) |
| minutes | Receives the minutes of the time stamp (between 0 and 59) |
| seconds | Receives the seconds of the time stamp (between 0 and 59) |
| milliseconds | Receives the milliseconds of the time stamp (between 0 and 999) |
| microseconds | Receives the microseconds of the time stamp (between 0 and 999) |
| nanoseconds (only form 2) | Receives the nanoseconds of the time stamp (between 0 and 999) |

## Return Values

—

## Example

```c
on envVar EnvGearUp
{
   dword d;
   byte h, m, s;
   word ms, us, ns;
   convertTimestampNS(timeNowNS(), d, h, m, s, ms, us, ns);
   write("Gear up at %d days, %d::%d::%d,%d.%d.%d", d, h, m, s, ms, us, ns);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 | 7.5 | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
