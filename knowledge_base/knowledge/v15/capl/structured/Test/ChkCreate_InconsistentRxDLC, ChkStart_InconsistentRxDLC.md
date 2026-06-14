# ChkCreate_InconsistentRxDLC, ChkStart_InconsistentRxDLC

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_InconsistentRxDLC(Node aNode, char [] aCallback);
dword ChkStart_InconsistentRxDLC(Node aNode, char [] aCallback);
```

## Description

Checks the DLC of all Rx messages of a node.

The check condition is violated if the DLC of the message does not agree with the DLC specified in the database.Can only be started in the "on start" area of CAPL or during the measurement. However, the check may be set up as early as in the "pre start" area.

## Parameters

| Name | Description |
|---|---|
| aNode | Must exist in the database. |
| aCallback | This parameter must be specified in simulation nodes; it is optional in test modules. |

## Example

```c
// checks the DLC of all Rx messages of the node
checkId = ChkStart_InconsistentRxDlc (NodeToObserve);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 7.0 SP5: method 7.2: extended | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN FlexRay | CAN FlexRay | — | CAN FlexRay | CAN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
