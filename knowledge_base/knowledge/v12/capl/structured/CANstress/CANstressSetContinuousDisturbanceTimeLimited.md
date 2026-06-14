# CANstressSetContinuousDisturbanceTimeLimited

> Category: `CANstress` | Type: `function`

## Syntax

```c
void CANstressSetContinuousDisturbanceTimeLimited (dword duration, dword type);
```

## Description

Sets the Continuous disturbance (time limited) mode. If the disturbance has not previously been terminated by means of an explicit command such as CANstressStop, the end of the test module or the end of the measurement, it will prevail for the period of time set in duration.

## Return Values

—

## Availability

| Since Version |
|---|
