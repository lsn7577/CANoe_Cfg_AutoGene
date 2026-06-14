# C2xGetCycleTime

> Category: `Car2x` | Type: `function`

## Syntax

```c
Int64 C2xGetCycleTime(char* dbMessage); //form 1
Int64 C2xGetCycleTime(char* dbMessage, char* stationName); //form 2
Int64 C2xGetCycleTime (long packetHandle); // form 3
Int64 C2xGetCycleTime (char stationName[], long packetHandle); // form 4
```

## Description

Gets the cycle time for a message in milliseconds.

## Parameters

| Name | Description |
|---|---|
| dbMessage | Name of the message |
| stationName | Name of the sending station |
| packetHandle | Packet handle of the message to be disabled. |

## Example

```c
Int64 cycleTime;
long packetHdl;

cycleTime = C2xGetCycleTime("CAM");

packetHdl = C2xGetMessageHandle (1,1);


cycleTime = C2xGetCycleTime (packetHdl);
cycleTime = C2xGetCycleTime ("BasicNode",packetHdl);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0: form 1 13.0: form 2, 3, 4 | — | — | — | 3.0: form 1 5.0: form 2, 3, 4 |
| Restricted To | — | Car2x: form 1, 3 Car2x, Testnodes: form 2, 4 | — | — | — | Car2x: form 1, 3 Car2x, Testnodes: form 2, 4 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
