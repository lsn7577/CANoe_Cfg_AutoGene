# ChkCreate_MostNetState, ChkStart_MostNetState

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostNetState(long aOldState, long aNewState);
dword ChkStart_MostNetState(long aOldState, long aNewState);
dword ChkCreate_MostNetState(long aOldState, long aNewState, Callback aCallback);
dword ChkStart_MostNetState(long aOldState, long aNewState, Callback aCallback);
```

## Description

This check is used to monitor the NetState state of the MOST hardware interface.

Concrete checks can be implemented for any NetState state changes, and are triggered when a NetState event having the corresponding target state occurs with a specified initial state.

The wildcard value –1 can be specified for one of the netstate parameters, if the check should monitor only the beginning or ending of a netstate. Both parameters can be set to wildcard value, if the check should detect any occurring netstate change.

This check always works on events. Therefore, it will not detect a current netstate, that has been established before the time of the check’s activation, as a new netstate.

## Parameters

| Name | Description |
|---|---|
| aCallback | Name of the callback function that is to be called when a specified state change occurs. This parameter must be set for simulation nodes; it is optional for test modules. |
| 0 | MostNetState_Undefined |
| 2 | MostNetState_PowerOff |
| 3 | MostNetState_NetInterfaceInit |
| 4 | MostNetState_ConfigNotOk |
| 5 | MostNetState_ConfigOk |
| -1 | Wildcard value (any state is matched) |
| aNewState | Target state of the state change to be monitored. Possible values the same as those for aOldState. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 7.0 SP5: method | — | — | — | — |
| Restricted To | — | MOST | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
