# ChkCreate_NodeDead, ChkStart_NodeDead

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_NodeDead (Node n, Duration aMaxQuietTime, char [] CaplCallback); // form 1
dword ChkStart_NodeDead (Node n, Duration aMaxQuietTime, char [] CaplCallback); // form 2
dword ChkStart_NodeDead (char [] Node, Duration aMaxQuietTime, char [] CaplCallback); // form 3
```

## Description

All monitored nodes must send at least one of their Tx messages within a specified interval. Otherwise an event will be triggered.

Gateway nodes require that the bus context corresponds to the bus that is being observed. This means that the check only works correctly if the current bus context corresponds to the database in which the node is defined.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

## Parameters

| Name | Description |
|---|---|
| n/Node | Defined node in database. |
| aMaxQuietTime | Upper limit of time interval. > 0; default unit [ms], if not changed with ChkConfig_SetPrecision. |
| CaplCallback | In simulation nodes this parameter has to be set.In test modules this parameter is optional. |

## Example

```c
// checks that at least one message of the node is sent in each 100 ms
checkId = ChkStart_NodeDead (100);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1: form 1, 2 7.0 SP5: method 8.5 SP2: form 3 9.0: form 3 replaced, method 3 | 13.0 | — | 14 | 1.0 2.1: form 3 replaced, method 3 |
| Restricted To | — | CAN FlexRay (since 7.2) | CAN FlexRay | — | CAN FlexRay | CAN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
