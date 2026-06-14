# addTimeToMeasurementStartTime

> Category: `Other` | Type: `function`

## Syntax

```c
long addTimeMeasurementStartTime(int64 timeSpan, long time[]);
```

## Description

Calculates the absolute date/time of the measurement start plus an offset (e.g. a timestamp).

In CANoeoffline mode, the function returns the oldest start time of those stored in the logging files.

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

| Since Version |
|---|
