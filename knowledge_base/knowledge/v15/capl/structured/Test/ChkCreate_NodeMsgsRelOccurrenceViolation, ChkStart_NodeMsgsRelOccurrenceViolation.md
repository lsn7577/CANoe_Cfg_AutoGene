# ChkCreate_NodeMsgsRelOccurrenceViolation, ChkStart_NodeMsgsRelOccurrenceViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_NodeMsgsRelOccurrenceViolation(Node observedNode, double aMinRelCycleTime, double aMaxRelCycleTime, char[] aCallback);
dword ChkStart_NodeMsgsRelOccurrenceViolation(Node observedNode, double aMinRelCycleTime, double aMaxRelCycleTime, char[] aCallback);
```

## Description

Checks for the occurrence of periodic message of the specified send node.The check condition is violated if the time between transmissions of the message is less than aMinRelCycleTime * GenMsgDelayTime or greater than aMaxRelCycleTime * Cycle Time.Cycle time is calculated from GenMsgCycleTime and GenSigCycleTime.Limits that should not be checked must be set to 0. At least one limit must be specified.Can only be started in the "on start" area of CAPL or during the measurement. However, the check may be set up as early as in the "pre start" area.

## Parameters

| Name | Description |
|---|---|
| observedNode | Must exist in the database. |
| aminRelCycleTime | 0: Limit is not checked. 0 < x < 1: Limit is checked. |
| aMaxRelCycleTime | 0: Limit is not checked. 1 < x < ∞: Limit is checked. |
| aCallback | This parameter must be specified in simulation nodes; it is optional in test modules. |

## Example

```c
// checks the periodic occurrence of all messages of the node
checkId = ChkStart_NodeMsgsRelOccurrenceViolation (NodeToObserve, 0.9, 1.1);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN FlexRay | CAN FlexRay | — | CAN FlexRay | CAN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
