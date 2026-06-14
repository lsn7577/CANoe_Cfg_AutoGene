# SetSender

> Category: `CommunicationObjects` | Type: `method`

## Syntax

```c
long txSignalRef::SetSender(char[] senderPath); // form 1
long rxSignalRef::SetSender(char[] senderPath);
long txPDURef::SetSender(char[] senderPath);
long rxPDURef::SetSender(char[] senderPath);
long txSignalRef::SetSender(dword senderIndex); // form 2
long rxSignalRef::SetSender(dword senderIndex);
long txPDURef::SetSender(dword senderIndex);
long rxPDURef::SetSender(dword senderIndex);
long txSignalRef::SetSender(COParticipant participant); // form 3
long rxSignalRef::SetSender(COParticipant participant);
long txPDURef::SetSender(COParticipant participant);
long rxPDURef::SetSender(COParticipant participant);
```

## Description

Sets the sender endpoint for the CO reference.

## Parameters

| Name | Description |
|---|---|
| senderPath (form 1) | Full path to a sender endpoint of the referenced object, including all namespaces. |
| senderIndex (form 2) | 0-based index of a sender endpoint of the referenced object. |
| participant (form 3) | A participant which contains a sender endpoint of the referenced object. |

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
