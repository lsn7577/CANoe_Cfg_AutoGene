# StmCreate_Ramp (limits user-defined)

> Category: `Test` | Type: `function`

## Syntax

```c
dword StmCreate_Ramp(message aMessage, dbsignal aDBSignal, double ValueA, double ValueB, dword CycleTime, dword TimeUp, dword TimeHigh, dword TimeDown, dword TimeLow); // form 1
dword StmCreate_Ramp(signal aDBSignal, double ValueA, double ValueB, dword CycleTime, dword TimeUp, dword TimeHigh, dword TimeDown, dword TimeLow); // form 2
dword StmCreate_Ramp(dbenvvar EnvVarHandle, double ValueA, double ValueB, dword CycleTime, dword TimeUp, dword TimeHigh, dword TimeDown, dword TimeLow); // form 3
dword StmCreate_Ramp(sysvar SystemVariable, double ValueA, double ValueB, dword CycleTime, dword TimeUp, dword TimeHigh, dword TimeDown, dword TimeLow); // form 4
dword StmCreate_Ramp(sysvar SystemVariable, int64 ValueA, int64 ValueB, dword CycleTime, dword TimeUp, dword TimeHigh, dword TimeDown, dword TimeLow); // form 5
```

## Description

Creates a stimulus generator that creates a ramp.

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
mId = StmCreate_Ramp(MsgBuf, Msg::Sig, ValueA, ValueB, CycleTime, Tup, Thigh, Tdown, Tlow);
To stimulate signals with the Interaction Layer:
mId = StmCreate_Ramp(Msg::Sig, ValueA, ValueB, CycleTime, Tup, Thigh, Tdown, Tlow);
mId = StmCreate_Ramp(EnvVarToStimulate, ValueA, ValueB, CycleTime, Tup, Thigh, Tdown, Tlow);
mId = StmCreate_Ramp(SysVarToStimulate, ValueA, ValueB, CycleTime, Tup, Thigh, Tdown, Tlow);
variables
{
message NewMessage aNewMessage;

mstimer mytimer;
dword yMin = 0;
dword yMax = 100;
dword ramp_cycletime = 50;
long stm_ramp;
}
on preStart
{
chkConfig_Init ("user");
stm_ramp = StmCreate_Ramp(aNewMessage, NewMessage::NewSignal, yMin, yMax, ramp_cycletime, 5000, 100, 0, 0);
}
on start
{
long ret;
ret = StmControl_Start(stm_ramp);
settimer (mytimer, ramp_cycletime);
}
on timer mytimer
{
if (yMax == aNewMessage.NewSignal) stmControl_Stop (stm_ramp);
output (aNewMessage);

settimer (mytimer, ramp_cycletime);
}
on preStop
{
StmControl_Destroy (stm_ramp);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 5.1: stimulate with IL 7.0 SP5: method 7.5: system variable support 8.5 SP3: function and method 5 | 13.0 | — | 14 | 1.0 2.0 SP2: function and method 5 |
| Restricted To | — | — | — | — | form 4, 5 | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
