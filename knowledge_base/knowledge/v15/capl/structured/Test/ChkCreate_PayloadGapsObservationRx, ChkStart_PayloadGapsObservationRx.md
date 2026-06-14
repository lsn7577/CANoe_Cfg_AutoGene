# ChkCreate_PayloadGapsObservationRx, ChkStart_PayloadGapsObservationRx

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_PayloadGapsObservationRx(Node aNode, long defaultBitValue, char [] aCallback);
dword ChkStart_PayloadGapsObservationRx(Node aNode, long defaultBitValue, char [] aCallback);
```

## Description

Checks the payload gaps and the DLC of all Rx messages of a node.

The check condition is violated if the payload gaps do not match the specified default bit value or the DLC does not match the specified DLC of the database.

## Parameters

| Name | Description |
|---|---|
| aNode | Must exist in the database. |
| defaultBitValue | Default bit value the payload gaps must have. |
| aCallback | This parameter must be specified in simulation nodes; it is optional in test modules. |

## Example

```c
/ checks the payload gaps of the message
checkId = ChkStart_PayloadGapsObservationRx(NodeToObserve, 0);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | 14 | 2.1 |
| Restricted To | — | CAN LIN FlexRay | CAN LIN FlexRay | — | CAN LIN FlexRay | CAN LIN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
