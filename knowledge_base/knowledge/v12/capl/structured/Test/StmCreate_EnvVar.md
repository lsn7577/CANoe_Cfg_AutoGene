# StmCreate_EnvVar

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_EnvVar(message aMessage, dbsignal aDBSignal, dbEnvVar aEnvVar, dword CycleTime);
```

## Description

Creates the stimulus with environment variables as data source.

## Example

To stimulate signals:

To stimulate signals with the Interaction Layer:

```c
mId = StmCreate_EnvVar(MsgBuf, Msg::Sig, EnvVar, CycleTime);
mId = StmCreate_EnvVar(Msg::Sig, EnvVar, CycleTime);
```

## Availability

| Since Version |
|---|
