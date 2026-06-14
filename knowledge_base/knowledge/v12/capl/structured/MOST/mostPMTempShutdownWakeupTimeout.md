# mostPMTempShutdownWakeupTimeout

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostPMTempShutdownWakeupTimeout (long timeout)
```

## Description

As described in the MOST specification in the chapter "Over-Temperature Management", the PowerMaster may try to wake-up the MOST ring, after a temperature shutdown, after a certain time. This function sets the timeout duration.

The default value is 60s.

By setting the "over temperature status" in the device of the PowerMaster, the wake-up attempt will not be performed after the timeout. After resetting the "over temperature status" the application has to perform the wake-up, if necessary.

## Return Values

See error codes

## Availability

| Since Version |
|---|
