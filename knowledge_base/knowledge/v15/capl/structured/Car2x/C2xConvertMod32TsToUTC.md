# C2xConvertMod32TsToUTC

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xConvertMod32TsToUTC( int64 mod32Ts, long refTime, long buffersize, long time[] )
```

## Description

This function converts a mod32 time stamp in milliseconds since a reference time into a UTC time stamp as array of type long with separate values for year, month, day, and so on.

## Parameters

| Name | Description |
|---|---|
| mod32Ts | Time stamp in milliseconds since the reference time. |
| refTime | The following reference times can be set: 0: 2004-01-01 (2004-01-01T00:00:00,000 UTC) 1: 2010-01-01 (2010-01-01T00:00:00,000 UTC). |
| buffersize | Size of the buffer to be filled with the UTC time stamp . |
| 0 | milliseconds (0..999) |
| 1 | seconds (0..60) |
| 2 | minutes (0..60) |
| 3 | hours (0..24) |
| 4 | day of month (1..31) |
| 5 | month (0..11) |
| 6 | year (starting with 1900) |
| 7 | day of week (0..7) |
| 8 | day of year (0..365) |

## Example

```c
enum enumRefTime{en2004 = 0, en2010 = 1};
long utcTime[9];

// milliseconds from 01.01.2004 00:00:00 UTC to 01.04.2019 00:00:00 UTC
int64 msSince2004 = 481161600000LL;

if (C2xConvertMod32TsToUTC(msSince2004, en2004, elCount(utcTime), utcTime) == 0)
{
  // output (leap seconds are considered): Date 2019-03-31 Time 23:59:55.000 UTC
  write("Date %d-%02d-%02d Time %02d:%02d:%02d.%03d UTC", 1900+utcTime[6], utcTime[5]+1, utcTime[4], utcTime[3], utcTime[2], utcTime[1], utcTime[0]);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12 SP2 | — | — | — | 4.0 SP2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
