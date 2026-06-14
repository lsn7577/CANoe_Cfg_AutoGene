# TestJoinMostPktEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinMostPktEvent(long aSourceAddress, long aDestinationAddress, char aPktDataDesc[], long aInstanceID)
long TestJoinMostPktEvent(long aSourceAddress, long aDestinationAddress, char aPktDataDesc[])
long TestJoinMostPktEvent(char aPktDataDesc[], long aInstanceID)
long TestJoinMostPktEvent(char aPktDataDesc[])
```

## Description

Adds an event condition for MOST packets to the current set of joined event conditions.

This function does not wait.

## Parameters

| Name | Description |
|---|---|
| Note For parameters aSourceAddress, aDestinationAddress, and aInstanceId the following applies: If -1 is given, the corresponding field can get any value. This is also the standard for not explicit set values. |  |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | — | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
