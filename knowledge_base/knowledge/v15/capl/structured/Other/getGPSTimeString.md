# getGPSTimeString

> Category: `Other` | Type: `function`

## Syntax

```c
void getGPSTimeString(char timeBuffer[], dword timestamp);
```

## Description

Copies a printed representation of the GPS time stamp represented as UTC date and time into the supplied character buffer. The format of the string is ddd mmm dd hh:mm:ss jjjj (e.g. "Fri Aug 21 15:22:24 1998").

## Parameters

| Name | Description |
|---|---|
| timeBuffer | The buffer the string will be written in.This buffer must be at least 26 characters long. |
| timestamp | The GPS time stamp (seconds have been displayed in time stamps since 1970-01-01, 00:00). The GPS time stamp is available as system variable as soon as a GPS device is configured. |

## Return Values

—

## Example

```c
variables
{
  char UTC_time_and_date_buffer[30]; // needs min. 26 chars
  dword UnixTimestamp;
}

on start
{
  getGPSTimeString(UTC_time_and_date_buffer, UnixTimestamp);
}
```

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
