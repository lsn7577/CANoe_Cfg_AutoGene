# linRegisterSchedulerStartStopCallback

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linRegisterSchedulerStartStopCallback (char[] callbackName);
```

## Description

Registers a callback function which is invoked if a LIN scheduler is either started or stopped.

## Parameters

| Name | Description |
|---|---|
| callbackName | The name of the callback function which should be registered. The callback must have the following signature: void func (dword channel, dword started, int64 eventTime) |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | 13.0 | — | 2.2 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
