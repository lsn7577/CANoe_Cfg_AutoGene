# SetReceiver

> Category: `CommunicationObjects` | Type: `method`

## Syntax

```c
long txSignalRef::SetReceiver(char[] receiverPath); // form 1
long rxSignalRef::SetReceiver(char[] receiverPath);
long txPDURef::SetReceiver(char[] receiverPath);
long rxPDURef::SetReceiver(char[] receiverPath);
long txSignalRef::SetReceiver(dword receiverIndex); // form 2
long rxSignalRef::SetReceiver(dword receiverIndex);
long txPDURef::SetReceiver(dword receiverIndex);
long rxPDURef::SetReceiver(dword receiverIndex);
long txSignalRef::SetReceiver(COParticipant participant); // form 3
long rxSignalRef::SetReceiver(COParticipant participant);
long txPDURef::SetReceiver(COParticipant participant);
long rxPDURef::SetReceiver(COParticipant participant);
```

## Description

Sets the receiver endpoint for the CO reference.

## Parameters

| Name | Description |
|---|---|
| receiverPath (form 1) | Full path to a receiver endpoint of the referenced object, including all namespaces. |
| receiverIndex (form 2) | 0-based index of a receiver endpoint of the referenced object. |
| participant (form 3) | A participant which contains a receiver endpoint of the referenced object. |

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
