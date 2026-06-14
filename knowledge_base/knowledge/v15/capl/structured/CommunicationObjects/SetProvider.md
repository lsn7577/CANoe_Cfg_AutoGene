# SetProvider

> Category: `CommunicationObjects` | Type: `method`

## Syntax

```c
long providedServiceRef::SetProvider(char[] providerPath); // form 1
long providedEventRef::SetProvider(char[] providerPath);
long providedFieldRef::SetProvider(char[] providerPath);
long providedPDURef::SetProvider(char[] providerPath);
long providedMethodRef::SetProvider(char[] providerPath);
long consumedServiceRef::SetProvider(char[] providerPath);
long consumedEventRef::SetProvider(char[] providerPath);
long consumedFieldRef::SetProvider(char[] providerPath);
long consumedPDURef::SetProvider(char[] providerPath);
long consumedMethodRef::SetProvider(char[] providerPath);
long serviceProviderRef::SetProvider(char[] providerPath);
long eventProviderRef::SetProvider(char[] providerPath);
long fieldProviderRef::SetProvider(char[] providerPath);
long pduProviderRef::SetProvider(char[] providerPath);
long providedServiceRef::SetProvider(dword index); // form 2
long providedEventRef::SetProvider(dword index);
long providedFieldRef::SetProvider(dword index);
long providedPDURef::SetProvider(dword index);
long providedMethodRef::SetProvider(dword index);
long consumedServiceRef::SetProvider(dword index);
long consumedEventRef::SetProvider(dword index);
long consumedFieldRef::SetProvider(dword index);
long consumedPDURef::SetProvider(dword index);
long consumedMethodRef::SetProvider(dword index);
long serviceProviderRef::SetProvider(dword index);
long eventProviderRef::SetProvider(dword index);
long fieldProviderRef::SetProvider(dword index);
long pduProviderRef::SetProvider(dword index);
long providedServiceRef::SetProvider(COParticipant participant); // form 3
long providedEventRef::SetProvider(COParticipant participant);
long providedFieldRef::SetProvider(COParticipant participant);
long providedPDURef::etProvider(COParticipant participant);
long providedMethodRef::SetProvider(COParticipant participant);
long consumedServiceRef::SetProvider(COParticipant participant);
long consumedEventRef::SetProvider(COParticipant participant);
long consumedFieldRef::SetProvider(COParticipant participant);
long consumedPDURef::SetProvider(COParticipant participant);
long consumedMethodRef::SetProvider(COParticipant participant);
long serviceProviderRef::SetProvider(COParticipant participant);
long eventProviderRef::SetProvider(COParticipant participant);
long fieldProviderRef::SetProvider(COParticipant participant);
long pduProviderRef::SetProvider(COParticipant participant);
long providedServiceRef::SetProvider(serviceProviderRef * provider); // form 4
long providedEventRef::SetProvider(eventProviderRef * provider);
long providedFieldRef::SetProvider(fieldProviderRef * provider);
long providedPDURef::SetProvider(pduProviderRef * provider);
long consumedServiceRef::SetProvider(serviceProviderRef * provider);
long consumedEventRef::SetProvider(eventProviderRef * provider);
long consumedFieldRef::SetProvider(fieldProviderRef * provider);
long consumedPDURef::SetProvider(pduProviderRef * provider);
```

## Description

Sets the provider endpoint for the CO reference.

## Parameters

| Name | Description |
|---|---|
| providerPath (form 1) | Full path to a provider endpoint of the referenced object, including all namespaces. |
| index (form 2) | 0-based index of a provider endpoint of the referenced object. |
| participant (form 3) | A participant which contains a provider endpoint of the referenced object. |
| provider (form 4) | A reference to a provider endpoint of the referenced object. |

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
