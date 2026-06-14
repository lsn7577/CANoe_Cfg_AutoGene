# J1939ILSetMsgPriority

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILSetMsgPriority(dbMsg dbMessage, dword priority ); // form 1
long J1939ILSetMsgPriority(dbNode node, dbMsg dbMessage, dword priority ); // form 2
```

## Description

Sets the message priority.

## Parameters

| Name | Description |
|---|---|
| dbMessage | message name as defined in the database |
| priority | priority of the message |
| node | Simulation node to apply the function |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2: form 1 12.0: form 2 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 | J1939 | — | — | form 2 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
