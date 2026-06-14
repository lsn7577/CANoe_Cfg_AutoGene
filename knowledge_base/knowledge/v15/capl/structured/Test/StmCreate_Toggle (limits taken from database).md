# StmCreate_Toggle (limits taken from database)

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_Toggle(message aMessage, dbsignal aDBSignal, dword CycleTime);
dword StmCreate_Toggle(signal aDBSignal, dword CycleTime);
dword StmCreate_Toggle(dbenvvar EnvVarHandle, dword CycleTime);
dword StmCreate_Toggle(sysvar SystemVariable, dword CycleTime);
```

## Description

Creates a stimulus generator that toggles between two values.

## Parameters

| Name | Description |
|---|---|
| aMessage | Must exist in DB |
| aDBSignal | Must exist in DB |
| EnvVarHandle | Must exist in DB |
| SystemVariable | Must be available in the configuration. |
| CycleTime | ms; 1 < x < ∞ Defines the cycle in which the signal value in the message buffer is being updated. There is no affect to the bus. Defines the cycle in which the value of the environment or system variable is being updated. |

## Return Values

Later this ID can be used to control the stimuli.

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
