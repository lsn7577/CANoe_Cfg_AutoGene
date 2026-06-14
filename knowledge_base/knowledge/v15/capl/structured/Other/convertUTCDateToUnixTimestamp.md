# convertUTCDateToUnixTimestamp

> Category: `Other` | Type: `function`

## Syntax

```c
Int64 convertUTCDateToUnixTimestamp(dword year, byte month, byte day, byte hour, byte minute, byte second);
```

## Description

Converts the given UTC time and date into a UNIX timestamp (seconds since 1970-01-01).

## Parameters

| Name | Description |
|---|---|
| year | The year. |
| month | The month (between 1 and 12). |
| day | The day (between 1 and 31). |
| hour | The hour (between 0 and 23). |
| minute | The minute (between 0 and 59). |
| second | The second (between 0 and 60, since leap seconds are supported). |

## Return Values

UNIX timestamp (seconds since 1970-01-01) corresponding to the input parameters.
-1 if input parameters are invalid

## Example

```c
stack Int64 unixTimestamp;
unixTimestamp = convertUTCDateToUnixTimestamp(2033, 05, 18, 03, 33, 20);
write("The unix timestamp will be %I64d", unixTimestamp);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 13.0 | 13.0 | 13.0 | — | 14 | 5.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
