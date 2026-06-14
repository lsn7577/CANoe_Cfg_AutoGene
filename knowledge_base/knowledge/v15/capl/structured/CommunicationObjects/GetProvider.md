# GetProvider

> Category: `CommunicationObjects` | Type: `method`

## Syntax

```c
COParticipant consumedServiceRef::GetProvider();
COParticipant consumedEventRef::GetProvider();
COParticipant consumedFieldRef::GetProvider();
COParticipant consumedPDURef::GetProvider();
COParticipant consumedMethodRef::GetProvider();
COParticipant providedServiceRef::GetProvider();
COParticipant providedEventRef::GetProvider();
COParticipant providedFieldRef::GetProvider();
COParticipant providedPDURef::GetProvider();
COParticipant providedMethodRef::GetProvider();
COParticipant serviceProviderRef::GetProvider();
COParticipant eventProviderRef::GetProvider();
COParticipant fieldProviderRef::GetProvider();
COParticipant pduProviderRef::GetProvider();
```

## Description

Returns the provider participant selected for the CO reference.

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
