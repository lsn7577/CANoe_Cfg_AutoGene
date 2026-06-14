# linSleepModeEvent

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void linSleepModeEvent(long syncTimeStamp, long origTimeStamp, int wasAwake, int isAwake, int externalCause, int reason)
```

## Description

Is called whenever a SleepModeEvent (not SleepModeFrame) is received. The time stamps are the same as by LINRcvFrame.

## Return Values

—

## Availability

| Up to Version |
|---|
