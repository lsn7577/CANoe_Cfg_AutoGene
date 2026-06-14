# linRegisterSchedulerStartStopCallback

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linRegisterSchedulerStartStopCallback (char[] callbackName)
```

## Description

Registers a callback function which is invoked if a LIN scheduler is either started or stopped.

This function may only be called in the event procedure on preStart.

## Return Values

Returns 1 if the registration succeeded, otherwise 0.

## Example

```c
on preStart
{
  linRegisterSchedulerStartStopCallback("OnSchedulerStartStop");
}

void OnSchedulerStartStop (dword channel, dword started, int64 eventTime)
{
  if (started)
  {
    write("Scheduler on LIN channel %ld started at: %lld", channel, eventTime);
  }
  else
  {
    write("Scheduler on LIN channel %ld stopped at: %lld", channel, eventTime);
  }
}
```

## Availability

| Since Version |
|---|
