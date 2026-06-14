# getMeasurementStartTime

> Category: `Other` | Type: `function`

## Syntax

```c
long getMeasurementStartTime(long time[]);
```

## Description

Returns details about the absolute time the measurement was started.

In CANoe offline mode, the function returns the oldest start time of those stored in the logging files.

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

| Since Version |
|---|
