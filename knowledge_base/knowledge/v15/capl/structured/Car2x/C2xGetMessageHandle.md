# C2xGetMessageHandle

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetMessageHandle(char* dbMessage); // form 1
long C2xGetMessageHandle(char* stationName, char* dbMessage); //form 2
long C2xGetMessageHandle(uint64 stationID, long sequenceNumber); //form 3
long C2xGetMessageHandle(char* stationName, uint64 stationID, long sequenceNumber); //form 4
```

## Description

This function returns the packet handle for a specified Car2x message.

Form 3 & 4 only work for stations where one or more DENMs are active.

## Parameters

| Name | Description |
|---|---|
| dbMessage | Name of the message |
| stationName | Name of the specified station |
| stationID | Id of the station that sends multiple DENM messages |
| sequenceNumber | Sequence number of the specified DENM messages |

## Example

```c
//Form 1: Single DENM or other application message
long handle;
handle= C2xGetMessageHandle("DENM");

//Form 3: Multiple DENM active

long eeblPacketHdl = 0;
long emcyPacketHdl = 0;
long rwwPacketHdl = 0;
long causeCode = 0;
eeblPacketHdl = C2xGetMessageHandle(1,1);
emcyPacketHdl = C2xGetMessageHandle(1,2);
rwwPacketHdl  = C2xGetMessageHandle(1,3);

causeCode=C2xGetTokenInt64(eeblPacketHdl,"DENM", "denm::situation::eventType::causeCode");
Write("EEBL CauseCode: %d", causeCode);
causeCode=C2xGetTokenInt64(emcyPacketHdl,"DENM", "denm::situation::eventType::causeCode");
Write("Emergency Vehicle CauseCode: %d", causeCode);
causeCode=C2xGetTokenInt64(rwwPacketHdl,"DENM", "denm::situation::eventType::causeCode");
Write("Roadworks CauseCode: %d", causeCode);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0: form 1, 2, 3, 4 | — | — | — | 5.0: form 1, 2, 3, 4 |
| Restricted To | — | Car2x: form 1, 3 Car2x Testnodes: 2, 4 | — | — | — | Car2x: form 1, 3 Car2x Testnodes: 2, 4 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
