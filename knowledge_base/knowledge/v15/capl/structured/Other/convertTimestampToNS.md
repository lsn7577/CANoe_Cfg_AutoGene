# convertTimestampToNS

> Category: `Other` | Type: `function`

## Syntax

```c
Int64 convertTimestampToNS ( dword days, dword hours, dword minutes, dword seconds );
```

## Description

Converts a time stamp given in days, hours, minutes and seconds into a nanosecond time stamp.

## Parameters

| Name | Description |
|---|---|
| days | Number of days of the time stamp. |
| hours | Number of hours of the time stamp. |
| minutes | Number of minutes of the time stamp. |
| seconds | Number of seconds of the time stamp. |

## Return Values

Time stamp in nanoseconds.

## Example

```c
variables
{
  dword days    = 432;
  dword hours   = 125;
  dword minutes = 102;
  dword seconds = 146;
}

on start
{
  write ("1 second = %I64d ns", ConvertTimestampToNS ( 0, 0, 0, 1 ));
  write ("1 minute = %I64d ns", ConvertTimestampToNS ( 0, 0, 1, 0 ));
  write ("1 hour   = %I64d ns", ConvertTimestampToNS ( 0, 1, 0, 0 ));
  write ("1 day    = %I64d ns", ConvertTimestampToNS ( 1, 0, 0, 0 ));

  write ("Sum of %d days %d hours %d minutes %d seconds = %I64d ns", days, hours, minutes, seconds, ConvertTimestampToNS ( days, hours, minutes, seconds ));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 14 | 14 | 14 | — | 14 | 5.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
