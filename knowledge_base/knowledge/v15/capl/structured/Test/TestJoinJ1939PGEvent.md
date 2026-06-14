# TestJoinJ1939PGEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinJ1939PGEvent (dbMsg aMessage)
long TestJoinJ1939PGEvent (dword aPGN)
long TestJoinJ1939PGEvent (dword aPGN, dword aSourceAddress, dword aDestinationAddress)
```

## Description

Completes the current set of joined events with the transmitted event.This function does not wait.

## Parameters

| Name | Description |
|---|---|
| aMessage | Message that should be awaited. Must be a J1939 parameter group. |
| aPGN | Parameter Group Number (with data page) of the message that should be awaited. |
| aSourceAddress | Source address of the message that should be awaited or 0xFFFFFFFF if source address is ignored. |
| aDestinationAddress | Destination address of the message that should be awaited or 0xFFFFFFFF if destination address is ignored. |

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
