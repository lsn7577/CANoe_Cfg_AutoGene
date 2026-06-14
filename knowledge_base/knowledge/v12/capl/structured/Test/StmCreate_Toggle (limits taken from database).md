# StmCreate_Toggle (limits taken from database)

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_Toggle(message aMessage, dbsignal aDBSignal, dword CycleTime);
```

## Description

Creates a stimulus generator that toggles between two values.

## Example

To stimulate signals:

To stimulate environment variables:

To stimulate system variables:

```c
mId = StmCreate_Toggle(MsgBuf, Msg::Sig, CycleTime);
To stimulate signals with the Interaction Layer:
mId = StmCreate_Toggle(Msg::Sig, CycleTime);
mId = StmCreate_Toggle(EnvVarToStimulate, CycleTime);
mId = StmCreate_Toggle(SysVarToStimulate, CycleTime);
```

## Availability

| Since Version |
|---|
