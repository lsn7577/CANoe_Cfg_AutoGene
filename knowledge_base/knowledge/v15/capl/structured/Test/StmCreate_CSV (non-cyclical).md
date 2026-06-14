# StmCreate_CSV (non-cyclical)

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_CSV(message aMessage, dbsignal aDBSignal, const char *aFile);
dword StmCreate_CSV(signal aDBSignal, const char *aFile);
dword StmCreate_CSV(dbenvvar EnvVarHandle, dbsignal aDBSignal, const char *aFile);
dword StmCreate_CSV(sysvar SystemVariable, dbsignal aDBSignal, const char *aFile);
```

## Description

Creates stimulus generator with csv file as data source.

## Parameters

| Name | Description |
|---|---|
| aMessage | Existing message (dbMsg type) in DB. |
| aDBSignal | Existing signal (dbSignal type) in DB. |
| aFile | Existing file to set the stimulus variable.If file not exists: EDI Invalid data input (measurement stops) |
| EnvVarHandle | Existing environment variable (EnvVar type) in DB. |
| SystemVariable | Existing system variable (sysVar type). |

## Return Values

Later this ID can be used to control the stimuli

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 5.1: stimulate with IL 7.0 SP5: method 7.5: system variable support | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
