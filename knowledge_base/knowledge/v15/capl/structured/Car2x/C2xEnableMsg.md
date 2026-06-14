# C2xEnableMsg

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xEnableMsg (char* dbMessage); //form 1
long C2xEnableMsg (char* dbMessage, char* stationName); //form 2
long C2xEnableMsg(long packetHandle); // form 3
long C2xEnableMsg (char stationName[], long packetHandle); // form 4
```

## Description

Enables a message for which the database attribute Send Type is Cyclic or CyclicIfActive in the database for cyclic sending. The function has no effect for messages with Send Type NoMsgSendType.

## Parameters

| Name | Description |
|---|---|
| dbMessage | Name of the message to be enabled |
| stationName | Name of the sending station |
| packetHandle | Packet handle of the message to be enabled. |

## Example

```c
long packetHdl =  -1;
C2xEnableMsg("CAM");
packetHdl = C2xGetMessageHandle(1,1);
C2xEnableMsg(packetHdl);
C2xEnableMsg ("BasicNode",packetHdl);
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
