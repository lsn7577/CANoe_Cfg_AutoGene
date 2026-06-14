# ChkCreate_NodeMsgsAbsDistViolation, ChkStart_ NodeMsgsAbsDistViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_NodeMsgsAbsDistViolation (Node aNode, Duration aMinTime, long aViolationsMaxCount, Duration aRatingPeriod);
dword ChkStart_NodeMsgsAbsDistViolation (Node aNode, Duration aMinTime, long aViolationsMaxCount, Duration aRatingPeriod);
dword ChkCreate_NodeMsgsAbsDistViolation (Node aNode, Duration aMinTime);
dword ChkStart_NodeMsgsAbsDistViolation (Node aNode, Duration aMinTime);
```

## Description

This check allows the supervision of the minimum send distance of all Tx messages of a node on one bus.

If no rating period and maximal number of distance undercuts is specified, the check condition fails if the time interval between two messages of the node undercuts the MinTime.

If the rating period and the maximal number of distance undercuts (> 0) are specified, the check observes the number of distance undercuts in a time slot. Exceeds the number of distance undercuts the allowed number in a time slot, the check fails.

## Parameters

| Name | Description |
|---|---|
| aNode | Must exist in DB. For Gateways the node name has to be prefixed by the bus name. |
| aMinTime | Minimum send distance of all Tx messages of the node. > 0; default unit [ms], if not changed with ChkConfig_SetPrecision. |
| aViolationsMaxCount | The number of allowed distance undercuts. |
| aRatingPeriod | Duration of the time slot, in which the maximal allowed number of distance undercuts is checked. > 0; default unit [ms], if not changed with ChkConfig_SetPrecision. |

## Example

```c
// checks the send distance between all Tx messages of the node
checkId = ChkStart_NodeMsgsAbsDistViolation(NodeToObserve, 30, 2, 40);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 SP3 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN | CAN | — | CAN | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
