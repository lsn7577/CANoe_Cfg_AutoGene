# StmCreate_Toggle (limits user-defined)

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_Toggle(message aMessage, dbsignal aDBSignal, double ValueA, double ValueB, dword CycleTime); // form 1
dword StmCreate_Toggle(signal aDBSignal, double ValueA, double ValueB, dword CycleTime); // form 2
dword StmCreate_Toggle(dbenvvar EnvVarHandle, double ValueA, double ValueB, dword CycleTime); // form 3
dword StmCreate_Toggle(sysvar SystemVariable, double ValueA, double ValueB, dword CycleTime); // form 4
dword StmCreate_Toggle(sysvar SystemVariable, int64 ValueA, double ValueB, int64 CycleTime); // form 5
```

## Description

Creates a stimulus generator that toggles between two values.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Return Values

Later this ID can be used to control the stimuli.

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 5.1: stimulate with IL 7.0 SP5: method 7.5: system variable support 8.5 SP3: form 5 | 13.0 | — | 14 | 1.0 2.0 SP2: form 5 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
