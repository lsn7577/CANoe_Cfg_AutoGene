# C2xSetCycleTime

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetCycleTime(char* dbMessage, int64 milliseconds); //form 1
long C2xSetCycleTime(char* dbMessage, int64 milliseconds, char* stationName); //form 2
long C2xDisableMsg(long packetHandle, int64 milliseconds); // form 3
long C2xDisableMsg(char stationName[], long packetHandle, int64 milliseconds); // form 4
```

## Description

Sets the cycle time for a message.

## Parameters

| Name | Description |
|---|---|
| dbMessage | Name of the message. |
| milliseconds | New cycle time in milliseconds. |
| stationName | Name of the sending station. |
| packetHandle | Packet handle of the message to check. |

## Example

```c
long packetHdl = -1;
C2xSetCycleTime("CAM", 1000);

packetHdl = C2xGetMessageHandle (1,1);
C2xSetCycleTime (1000, packetHdl);

C2xSetCycleTime ("BasicNode", 1000, packetHdl);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0: form 1 13.0: form 2, 3, 4 | — | — | — | 2.1 SP3: form 1 5.0: form 2, 3, 4 |
| Restricted To | — | Car2x: 1, 3 Car2x, Testnodes: 2, 4 | — | — | — | Car2x: 1, 3 Car2x, Testnodes: 2, 4 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
