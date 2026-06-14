# TestWaitForMostNetState

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostNetState(long aOldState, long aNewState, unsigned long aTimeout);
```

## Description

The function waits until the expiration of the time aTimeout for a transfer of the MOST NetState from the state aOldState into the state aNewState.

## Parameters

| Name | Description |
|---|---|
| 0 | MostNetState_Undefined |
| 2 | MostNetState_PowerOff |
| 3 | MostNetState_NetInterfaceInit |
| 4 | MostNetState_ConfigNotOk |
| 5 | MostNetState_ConfigOk |
| -1 | Wildcard, any NetState state |
| aNewState | Expected new state of the NetState. The value range corresponds to that of aOldState Parameters. |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout monitoring) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | — | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
