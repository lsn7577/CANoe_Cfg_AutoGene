# StmCreate_Ramp (limits user-defined)

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_Ramp(message aMessage, dbsignal aDBSignal, double ValueA, double ValueB, dword CycleTime, dword TimeUp, dword TimeHigh, dword TimeDown, dword TimeLow); // form 1
```

## Description

Creates a stimulus generator that creates a ramp.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Example

To stimulate signals:

To stimulate environment variables:

To stimulate system variables:

```c
mId = StmCreate_Ramp(MsgBuf, Msg::Sig, ValueA, ValueB, CycleTime, Tup, Thigh, Tdown, Tlow);
To stimulate signals with the Interaction Layer:
mId = StmCreate_Ramp(Msg::Sig, ValueA, ValueB, CycleTime, Tup, Thigh, Tdown, Tlow);
mId = StmCreate_Ramp(EnvVarToStimulate, ValueA, ValueB, CycleTime, Tup, Thigh, Tdown, Tlow);
mId = StmCreate_Ramp(SysVarToStimulate, ValueA, ValueB, CycleTime, Tup, Thigh, Tdown, Tlow);
```

## Availability

| Since Version |
|---|
