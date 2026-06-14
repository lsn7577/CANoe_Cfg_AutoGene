# C2xSendMsg

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSendMsg(char* dbMessage); //form 1
long C2xSendMsg(char* dbMessage, char* stationName); //form 2
long C2xSendMsg (long packetHandle); // form 3
long C2xSendMsg (char stationName[], long packetHandle); // form 4
```

## Description

Send the message with the specified message name.

## Parameters

| Name | Description |
|---|---|
| dbMessage | Name of the message to send. |
| stationName | Name of the sending station. |
| packetHandle | Packet handle of the message to check. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0: form 1 13.0: form 2, 3, 4 | — | — | — | 2.1 SP3: form 1 5.0: form 2, 3, 4 |
| Restricted To | — | Car2x: form 1, 3 Car2x, Testnodes: 2, 4 | — | — | — | Car2x: form 1, 3 Car2x, Testnodes: 2, 4 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
