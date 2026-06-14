# ChkCreate_AllNodesDead, ChkStart_AllNodesDead

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_AllNodesDead (Duration aMaxQuietTime, char [] CaplCallback);
dword ChkStart_AllNodesDead (Duration aMaxQuietTime, char [] CaplCallback);
```

## Description

All monitored nodes must send at least one of their Tx messages within a specified interval. Otherwise an event will be triggered.

Each node is checked separately, so a dead node is recognized even if others are alive.

Gateway nodes require that the bus context corresponds to the network that is being observed.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

## Parameters

| Name | Description |
|---|---|
| aMaxQuietTime | Upper limit of time interval. > 0; default unit [ms], if not changed with ChkConfig_SetPrecision. |
| CaplCallback | In simulation nodes this parameter has to be set.In test modules this parameter is optional. |

## Example

```c
// checks that at least one message is sent in each 100 ms
checkId = ChkStart_AllNodesDead (100);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 7.0 SP5: method 7.2: extended | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN FlexRay | CAN FlexRay | — | CAN FlexRay | CAN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
