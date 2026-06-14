# TestWaitForMostSpyPkt

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostSpyPkt(long aSourceAddress, long aDestinationAddress, char aPktDataDesc[], long aInstanceID, dword aTimeout);
long TestWaitForMostSpyPkt(long aSourceAddress, long aDestinationAddress, char aPktDataDesc[], dword aTimeout);
long TestWaitForMostSpyPkt(char aPktDataDesc[], long aInstanceID, dword aTimeout);
long TestWaitForMostSpyPkt(char aPktDataDesc[], dword aTimeout);
```

## Description

Waits for the occurrence of the specified MOST (spy) packet. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

The first and third signatures are exclusively suited to set up wait conditions for packets having function catalog format, whereas the other signatures also allow the definition of raw packets.

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
