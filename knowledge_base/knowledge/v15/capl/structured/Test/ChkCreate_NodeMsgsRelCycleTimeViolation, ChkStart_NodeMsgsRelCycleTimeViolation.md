# ChkCreate_NodeMsgsRelCycleTimeViolation, ChkStart_NodeMsgsRelCycleTimeViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_NodeMsgsRelCycleTimeViolation (Node aNode, double aMinRelCycleTime, double aMaxRelCycleTime, Callback aCallback);
dword ChkStart_NodeMsgsRelCycleTimeViolation (Node aNode, double aMinRelCycleTime, double aMaxRelCycleTime, Callback aCallback);
```

## Description

Checks the occurrences of cyclic messages of the given send node.

Event is generated if the time between sends of the (same) message is smaller than minRelCycleTime * GenMsgCycleTime (DB-attribute) or larger than maxRelCycleTime * GenMsgCycleTime.

Not to be checked limits are set to 0; there must be at least on limit specified.

Not checked are send messages with a specified cycle time equal to 0 or network management messages or diagnostic messages.

Can be started only in the start-section of CAPL or during measurement.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

## Parameters

| Name | Description |
|---|---|
| aNode | Must exist in DB |
| aMinRelCycleTime | 0: Limit is not checked0 < x < 1: Limit is checked |
| aMaxRelCycleTime | 0: Limit is not checked1 < x < ∞: Limit is checked |
| aCallback | In simulation nodes this parameter has to be set.In test modules this parameter is optional. |

## Example

```c
// checks the cycle time of all messages of the node
checkId = ChkStart_NodeMsgsRelCycleTimeViolation (NodeToObserve, 0.9, 1.1);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN FlexRay | CAN FlexRay | — | CAN FlexRay | CAN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
