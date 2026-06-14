# StmCreate_CSV (cyclical)

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_CSV(message aMessage, dbsignal aDBSignal, dword CycleTime, const char *aFile);
```

## Description

Creates stimulus generator with csv file as data source.

## Example

To stimulate signals:

To stimulate signals with the Interaction Layer:

To stimulate environment variables:

To stimulate system variables:

```c
mId = StmCreate_CSV(MsgBuf, Msg::Sig, CycleTime, File);
mId = StmCreate_CSV(Msg::Sig, CycleTime, File);
mId = StmCreate_CSV(EnvVarToStimulate, Msg::Sig, CycleTime, File);
mId = StmCreate_CSV(SysVarToStimulate, Msg::Sig, CycleTime, File);
```

## Availability

| Since Version |
|---|
