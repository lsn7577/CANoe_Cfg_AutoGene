# C2xConvertTimeToMSSinceUTC

> Category: `Car2x` | Type: `function`

## Syntax

```c
int64 C2xConvertTimeToMSSinceUTC( int64 itsTimestamp, long refTime ); // form 1
int64 C2xConvertTimeToMSSinceUTC( long year, long month, long day, long hours, long minutes, long seconds, long milliseconds, long refTime ); // form 2
```

## Description

This function returns the elapsed milliseconds between a reference time and a time stamp.

As time stamp input either a Unix time stamp in milliseconds (form 1) or a UTC time given with year, month, hour and so on as separate parameters (form 2) can be given. Specific reference times can be set as additional parameter.

The result can be used for the time stamps defined in e.g. a CAM or a DENM.

## Parameters

| Name | Description |
|---|---|
| itsTimestamp | Unix time stamp in milliseconds (time zone UTC) |
| year | Year of the UTC time stamp |
| month | Month of the UTC time stamp (1..12) |
| day | Day of the UTC time stamp (1..31) |
| hours | Hours of the UTC time stamp since midnight (0..23) |
| minutes | Minutes of the UTC time stamp after the hour (0..59) |
| seconds | Seconds of the UTC time stamp after the minute (0..59) |
| milliseconds | Milliseconds of the UTC time stamp after the second (1..999) |
| refTime | The following reference times can be set: 2004-01-01 = 0 (2004-01-01T00:00:00,000 UTC) 2010-01-01 = 1 (2010-01-01T00:00:00,000 UTC) |

## Example

```c
int64 itsTimestamp = 0; // original time stamp
int64 itsTS2004 = 0; // converted to 2004 format
word itsTS2004mod16unsigned = 0; // -> mod16 unsigned
long itsTS2004mod32signed = 0; // -> mod32 signed
int64 itsTS2010 = 0; // converted to 2010 format
enum enumRefTime{en2004 = 0, en2010 = 1};

// get times tamp once
itsTimestamp = C2xGetITSTimestamp();

// convert time stamps into needed formats
itsTS2004 = C2xConvertTimeToMSSinceUTC(itsTimestamp, en2004);
itsTS2004mod16unsigned = C2xConvertTimeToMSSinceUTC(itsTimestamp, en2004) & 0xFFFFFFFF;
itsTS2004mod32signed = C2xConvertTimeToMSSinceUTC(itsTimestamp, en2004) & 0x7FFFFFFFFFFFFFFFLL;
itsTS2010 = C2xConvertTimeToMSSinceUTC(itsTimestamp, en2010);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
