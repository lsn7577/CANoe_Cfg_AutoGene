# ChkCreate_AllNodesBabbling, ChkStart_AllNodesBabbling

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_AllNodesBabbling (Duration aMinQuietTime, char [] CaplCallback);
dword ChkStart_AllNodesBabbling (Duration aMinQuietTime, char [] CaplCallback);
```

## Description

There is a time interval where transmissions are tolerated. After the interval has been passed, all nodes may no longer send messages. From now on, each transmission of the nodes is reported.

If the min. quiet time is 0, then each message sent by any node leads to the event.

Possible application: Supervises the end of a communication. Supervises the transition of nodes’ or buses’ state to "sleep active".

Gateway nodes require that the bus context corresponds to the network that is being observed.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

## Parameters

| Name | Description |
|---|---|
| aMinQuietTime | > 0; default unit [ms], if not changed with ChkConfig_SetPrecision. |
| CaplCallback | In simulation nodes this parameter has to be set.In test modules this parameter is optional. |

## Example

```c
// checks that after 300 ms no transmission are available
checkId = ChkStart_AllNodesBabbling(300);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 7.0 SP5: method 7.2: extended | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN FlexRay | CAN FlexRay | — | CAN FlexRay | CAN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
