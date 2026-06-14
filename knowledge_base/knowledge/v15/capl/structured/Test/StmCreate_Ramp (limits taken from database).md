# StmCreate_Ramp (limits taken from database)

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_Ramp(message aMessage, dbsignal aDBSignal, dword CycleTime, dword TimeUp, dword TimeHigh, dword TimeDown, dword TimeLow);
dword StmCreate_Ramp(signal aDBSignal, dword CycleTime, dword TimeUp, dword TimeHigh, dword TimeDown, dword TimeLow);
dword StmCreate_Ramp(dbenvvar EnvVarHandle, dword CycleTime, dword TimeUp, dword TimeHigh, dword TimeDown, dword TimeLow);
dword StmCreate_Ramp(sysvar SystemVariable, dword CycleTime, dword TimeUp, dword TimeHigh, dword TimeDown, dword TimeLow);
```

## Description

Creates a stimulus generator that creates a ramp.

## Parameters

| Name | Description |
|---|---|
| aMessage | Existing message (dbMsg type) in DB |
| aDBSignal | Existing signal (dbSignal type) in DB |
| EnvVarHandle | Existing environment variable (EnvVar type) in DB |
| SystemVariable | Must be available in the configuration. |
| CycleTime | ms; 1 < x < ∞ Defines the cycle in which the signal value in the message buffer is being updated. There is no affect to the bus. Defines the cycle in which the value of the environment or system variable is being updated. |
| Note For more information please see Stimulus Generator: Creating a Ramp. |  |
| Note For more information please see Stimulus Generator: Creating a Ramp. |  |
| Note Time Up = Time High = Time Down = 0: ESE Invalid stimuli effect (measurement stops) For more information please see Stimulus Generator: Creating a Ramp. |  |
| Note For more information please see Stimulus Generator: Creating a Ramp. |  |

## Return Values

Later this ID can be used to control the stimuli

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
