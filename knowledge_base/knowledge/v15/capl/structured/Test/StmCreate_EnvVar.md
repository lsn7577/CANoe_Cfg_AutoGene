# StmCreate_EnvVar

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_EnvVar(message aMessage, dbsignal aDBSignal, dbEnvVar aEnvVar, dword CycleTime);
dword StmCreate_EnvVar(signal aDBSignal, dbEnvVar aEnvVar, dword CycleTime);
```

## Description

Creates the stimulus with environment variables as data source.

## Parameters

| Name | Description |
|---|---|
| aMessage | Must exist in DB |
| aDBSignal | Must exist in DB |
| aEnvVar | Must exist in DB |
| CycleTime | ms; 1 < x < ∞ Defines the cycle in which the signal value in the message buffer is being updated. There is no affect to the bus. |

## Return Values

Later this ID can be used to control the stimuli

## Example

To stimulate signals:

To stimulate signals with the Interaction Layer:

```c
mId = StmCreate_EnvVar(MsgBuf, Msg::Sig, EnvVar, CycleTime);
mId = StmCreate_EnvVar(Msg::Sig, EnvVar, CycleTime);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 5.1: stimulate with IL 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
