# GetConsumer

> Category: `CommunicationObjects` | Type: `method`

## Syntax

```c
COParticipant consumedServiceRef::GetConsumer();
COParticipant consumedEventRef::GetConsumer();
COParticipant consumedFieldRef::GetConsumer();
COParticipant consumedMethodRef::GetConsumer();
COParticipant consumedPDURef::GetConsumer();
COParticipant providedServiceRef::GetConsumer();
COParticipant providedEventRef::GetConsumer();
COParticipant providedFieldRef::GetConsumer();
COParticipant providedPDURef::GetConsumer();
COParticipant providedMethodRef::GetConsumer();
COParticipant serviceConsumerRef::GetConsumer();
COParticipant eventConsumerRef::GetConsumer();
COParticipant fieldConsumerRef::GetConsumer();
COParticipant pduConsumerRef::GetConsumer();
```

## Description

Returns the consumer participant selected for the CO reference.

## Return Values

If the object is valid and refers to an endpoint which is assigned to a participant, returns a reference to that participant. Else returns an invalid reference.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | 15 | 14 | 5.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
