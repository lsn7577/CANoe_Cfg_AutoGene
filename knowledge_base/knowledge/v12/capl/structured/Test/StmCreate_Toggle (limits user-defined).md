# StmCreate_Toggle (limits user-defined)

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_Toggle(message aMessage, dbsignal aDBSignal, double ValueA, double ValueB, dword CycleTime); // form 1
```

## Description

Creates a stimulus generator that toggles between two values.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Example

To stimulate signals:

To stimulate environment variables:

To stimulate system variables:

```c
mId = StmCreate_Toggle(MsgBuf, Msg::Sig, ValueA, ValueB, CycleTime);
To stimulate signals with the Interaction Layer:
mId = StmCreate_Toggle(Msg::Sig, ValueA, ValueB, CycleTime);

mId = StmCreate_Toggle(EnvVarToStimulate, ValueA, ValueB, CycleTime);
mId = StmCreate_Toggle(SysVarToStimulate, ValueA, ValueB, CycleTime);
```

## Availability

| Since Version |
|---|
