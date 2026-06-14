# C2xTestWaitForSignalInRange

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xTestWaitForSignalInRange (char* protocolDesignator, char* tokenDesignator, int64 minTokenValue, int64 maxTokenValue, long timeout) // form 1
long C2xTestWaitForSignalInRange (char* protocolDesignator, char* tokenDesignator, int64 minTokenValue, int64 maxTokenValue, char* stationName, long timeout) // form 2
```

## Description

Waits for the occurrence of the first Car2x message with a signal that is inside or equals the given limit. Should the message not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| protocolDesignator | Protocol designator of the Car2x message that should be awaited. |
| tokenDesignator | Token designator of the Car2x message that should be awaited. |
| minTokenValue | Lower limit of the value. |
| maxTokenValue | Upper limit of the value. |
| stationName | Name of the sender station of the Car2x message that should be awaited. |
| aTimeout | Maximum time that should be waited [ms]. Transmission of 0: no timeout controlling. |

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
