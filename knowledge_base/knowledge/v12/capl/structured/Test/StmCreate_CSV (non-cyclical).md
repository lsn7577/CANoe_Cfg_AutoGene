# StmCreate_CSV (non-cyclical)

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_CSV(message aMessage, dbsignal aDBSignal, const char *aFile);
```

## Description

Creates stimulus generator with csv file as data source.

## Example

To stimulate signals:

To stimulate signals with the Interaction Layer:

To stimulate environment variables:

To stimulate system variables:

```c
mId = StmCreate_CSV(MsgBuf, Msg::Sig, File);
mId = StmCreate_CSV(Msg::Sig, File);
mId = StmCreate_CSV(EnvVarToStimulate, Msg::Sig, File);
mId = StmCreate_CSV(SysVarToStimulate, Msg::Sig, File);
```

## Availability

| Since Version |
|---|
