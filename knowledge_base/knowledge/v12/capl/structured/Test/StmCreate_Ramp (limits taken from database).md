# StmCreate_Ramp (limits taken from database)

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_Ramp(message aMessage, dbsignal aDBSignal, dword CycleTime, dword TimeUp, dword TimeHigh, dword TimeDown, dword TimeLow);
```

## Description

Creates a stimulus generator that creates a ramp.

## Example

To stimulate signals:

To stimulate environment variables:

To stimulate system variables:

```c
mId = StmCreate_Ramp(MsgBuf, Msg::Sig, CycleTime, Tup, Thigh, Tdown, Tlow);
To stimulate signals with the Interaction Layer:
mId = StmCreate_Ramp(Msg::Sig, CycleTime, Tup, Thigh, Tdown, Tlow);
mId = StmCreate_Ramp(EnvVarToStimulate, CycleTime, Tup, Thigh, Tdown, Tlow);
mId = StmCreate_Ramp(SysVarToStimulate, CycleTime, Tup, Thigh, Tdown, Tlow);
```

## Availability

| Since Version |
|---|
