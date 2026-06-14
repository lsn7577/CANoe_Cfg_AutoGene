# GetProviderIndex

> Category: `CommunicationObjects` | Type: `method`

## Syntax

```c
long consumedServiceRef::GetProviderIndex();
long consumedEventRef::GetProviderIndex();
long consumedFieldRef::GetProviderIndex ();
long consumedPDURef::GetProviderIndex ();
long consumedMethodRef::GetProviderIndex ();
long providedServiceRef::GetProviderIndex ();
long providedEventRef::GetProviderIndex ();
long providedFieldRef::GetProviderIndex ();
long providedPDURef::GetProviderIndex ();
long providedMethodRef::GetProviderIndex ();
long serviceProviderRef::GetProviderIndex ();
long eventProviderRef::GetProviderIndex ();
long fieldProviderRef::GetProviderIndex ();
long pduProviderRef::GetProviderIndex ();
```

## Description

Returns the provider index selected for the CO reference.

## Return Values

If the object is valid and refers to a valid endpoint, returns the index of that endpoint. Else returns -1.

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
