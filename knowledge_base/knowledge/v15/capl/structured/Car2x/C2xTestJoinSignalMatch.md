# C2xTestJoinSignalMatch

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xTestJoinSignalMatch (char* protocolDesignator, char* tokenDesignator, int64 tokenValue) // form 1
long C2xTestJoinSignalMatch (char* protocolDesignator, char* tokenDesignator, int64 tokenValue, char* stationName) // form 2
```

## Description

Completes the current set of joined events with the transmitted event. This function does not wait.

## Parameters

| Name | Description |
|---|---|
| protocolDesignator | Protocol designator of the Car2x message that should be awaited. |
| tokenDesignator | Token designator of the Car2x message that should be awaited. |
| tokenValue | Token value that should be awaited. |
| stationName | Name of the sender station of the Car2x message that should be awaited. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0: form 1, 2 | — | — | — | 5.0: form 1, 2 |
| Restricted To | — | Car2x, Testnodes: form 1, 2 | — | — | — | Car2x: form 1, 2 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
