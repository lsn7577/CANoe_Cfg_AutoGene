# ChkCreate_NodeBabbling, ChkStart_NodeBabbling

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_NodeBabbling (Node n, Duration aMinQuietTime, char [] CaplCallback); // form 1
dword ChkStart_NodeBabbling (Node n, Duration aMinQuietTime, char [] CaplCallback); // form 2
dword ChkStart_NodeBabbling (char [] Node, Duration aMinQuietTime, char [] CaplCallback); // form 3
```

## Description

This check supervises the end of a communication: There is a time interval where node-transmissions are tolerated. After the interval has been passed, the node may no longer send messages. From now on, each transmission of the node is reported.

If the min. quiet time is 0, then each message sent by the node leads to the event.

Use Cases:Supervise the transition of nodes’ or busses’ state to 'sleep active'.

Gateway nodes require that the bus context corresponds to the bus that is being observed. This means that the check only works correctly if the current bus context corresponds to the database in which the node is defined.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

## Parameters

| Name | Description |
|---|---|
| n/Node | Defined node in database. |
| aMinQuietTime | > 0; default unit [ms], if not changed with ChkConfig_SetPrecision. |
| CaplCallback | In simulation nodes this parameter has to be set.In test modules this parameter is optional. |

## Example

```c
// checks that after 300 ms no transmission of the node is available
checkId = ChkStart_NodeBabbling(NodeToObserve, 300);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1: form 1, 2 7.0 SP5: methods 1 and 2: form 1 8.5 SP2: form 3 9.0: form 3 replaced, method 3 | 13.0 | — | 14 | 1.0 2.1: : form 3 replaced, method 3 |
| Restricted To | — | CAN FlexRay (since 7.2) | CAN FlexRay | — | CAN FlexRay | CAN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
