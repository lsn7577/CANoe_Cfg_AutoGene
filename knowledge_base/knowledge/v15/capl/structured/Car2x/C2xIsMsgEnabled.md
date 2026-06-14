# C2xIsMsgEnabled

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xIsMsgEnabled (char* dbMessage); //form 1
long C2xIsMsgEnabled (char* dbMessage, char* stationName); //form 2
long C2xIsMsgEnabled (long packetHandle); // form 3
long C2xIsMsgEnabled (char stationName[], long packetHandle); // form 4
```

## Description

Check if a message is enabled for cyclic sending.

## Parameters

| Name | Description |
|---|---|
| dbMessage | Name of the message to check. |
| stationName | Name of the sending station. |
| packetHandle | Packet handle of the message to check. |

## Example

```c
LONG result = 0;
long packetHdl = -1;
result = C2xIsMsgEnabled("CAM");

packetHdl = C2xGetMessageHandle (1,1);
result = C2xIsMsgEnabled (packetHdl);

result = C2xIsMsgEnabled ("BasicNode",packetHdl);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0: form 1 13.0: form 2, 3, 4 | — | — | — | 2.2: form 1 5.0: form 2, 3, 4 |
| Restricted To | — | Car2x: form 1, 3 Car2x, Testnodes: form 2, 4 | — | — | — | Car2x: form 1, 3 Car2x, Testnodes: form 2, 4 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
