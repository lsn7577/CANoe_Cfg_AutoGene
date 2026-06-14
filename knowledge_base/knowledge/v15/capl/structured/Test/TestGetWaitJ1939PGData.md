# TestGetWaitJ1939PGData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitJ1939PGData (pg * aPG); // form 1
long TestGetWaitJ1939PGData (dword index, pg * aPG); // form 2
```

## Description

If a J1939 parameter group event is the last event that triggers a wait instruction, the message content can be called up with the first function.

The second function can only be used for joined events. The number of the joined event (return value of testJoin...) is here being used as an index.

## Parameters

| Name | Description |
|---|---|
| aPG | J1939 parameter group variable that should be filled with this function. |
| index | Number of the joined event corresponds with the return value of testJoin.... |

## Example

```c
// add J1939 PG event to the current set of “joined events” and fill the parameter group data to parameter group ‘eventMessage’

pg TSC1 pgTSC1;
dword index = 0;
TestJoinJ1939PGEvent (TSC1);
// ... other join events
index = TestWaitForAllJoinedEvents (2000);

TestGetWaitJ1939PGData (index, pgTSC1);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
