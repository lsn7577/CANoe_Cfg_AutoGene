# SetConsumer

> Category: `CommunicationObjects` | Type: `method`

## Syntax

```c
long consumedServiceRef::SetConsumer(char[] consumerPath); // form 1
long consumedEventRef::SetConsumer(char[] consumerPath);
long consumedFieldRef::SetConsumer(char[] consumerPath);
long consumedPDURef::SetConsumer(char[] consumerPath);
long consumedMethodRef::SetConsumer(char[] consumerPath);
long providedServiceRef::SetConsumer(char[] consumerPath);
long providedEventRef::SetConsumer(char[] consumerPath);
long providedFieldRef::SetConsumer(char[] consumerPath);
long providedPDURef::SetConsumer(char[] consumerPath);
long providedMethodRef::SetConsumer(char[] consumerPath);
long serviceConsumerRef::SetConsumer(char[] consumerPath);
long eventConsumerRef::SetConsumer(char[] consumerPath);
long fieldConsumerRef::SetConsumer(char[] consumerPath);
long pduConsumerRef::SetConsumer(char[] consumerPath);
long consumedServiceRef::SetConsumer(dword index); // form 2
long consumedEventRef::SetConsumer(dword index);
long consumedFieldRef::SetConsumer(dword index);
long consumedPDURef::SetConsumer(dword index);
long consumedMethodRef::SetConsumer(dword index);
long providedServiceRef::SetConsumer(dword index);
long providedEventRef::SetConsumer(dword index);
long providedFieldRef::SetConsumer(dword index);
long providedPDURef::SetConsumer(dword index);
long providedMethodRef::SetConsumer(dword index);
long serviceConsumerRef::SetConsumer(dword index);
long eventConsumerRef::SetConsumer(dword index);
long fieldConsumerRef::SetConsumer(dword index);
long pduConsumerRef::SetConsumer(dword index);
long consumedServiceRef::SetConsumer(COParticipant participant); // form 3
long consumedEventRef::SetConsumer(COParticipant participant);
long consumedFieldRef::SetConsumer(COParticipant participant);
long consumedPDURef::SetConsumer(COParticipant participant);
long consumedMethodRef::SetConsumer(COParticipant participant);
long providedServiceRef::SetConsumer(COParticipant participant);
long providedEventRef::SetConsumer(COParticipant participant);
long providedFieldRef::SetConsumer(COParticipant participant);
long providedPDURef::SetConsumer(COParticipant participant);
long providedMethodRef::SetConsumer(COParticipant participant);
long serviceConsumerRef::SetConsumer(COParticipant participant);
long eventConsumerRef::SetConsumer(COParticipant participant);
long fieldConsumerRef::SetConsumer(COParticipant participant);
long pduConsumerRef::SetConsumer(COParticipant participant);
long consumedServiceRef::SetConsumer(serviceConsumerRef * consumer); // form 4
long consumedEventRef::SetConsumer(eventConsumerRef * consumer);
long consumedFieldRef::SetConsumer(fieldConsumerRef * consumer);
long consumedPDURef::SetConsumer(pduConsumerRef * consumer);
long providedServiceRef::SetConsumer(serviceConsumerRef * consumer);
long providedEventRef::SetConsumer(eventConsumerRef * consumer);
long providedFieldRef::SetConsumer(fieldConsumerRef * consumer);
long providedPDURef::SetConsumer(pduConsumerRef * consumer);
```

## Description

Sets the consumer endpoint for the CO reference.

## Parameters

| Name | Description |
|---|---|
| consumerPath (form 1) | Full path to a consumer endpoint of the referenced object, including all namespaces. |
| index (form 2) | 0-based index of a consumer endpoint of the referenced object. |
| participant (form 3) | A participant which contains a consumer endpoint of the referenced object. |
| consumer (form 4) | A reference to a consumer endpoint of the referenced object. |

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
