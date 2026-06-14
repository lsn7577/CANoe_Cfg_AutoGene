# Iso11783IL_TIMDisconnectFromServer

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMDisconnectFromServer(dbNode server); // form 1
long Iso11783IL_TIMDisconnectFromServer(byte serverAddress); // form 2
long Iso11783IL_TIMDisconnectFromServer(dbNode server, dword options); // form 3
long Iso11783IL_TIMDisconnectFromServer(bytes serverAddress, dword options); // form 4
long Iso11783IL_TIMDisconnectFromServer(dbNode client, dbNode server); // form 5
long Iso11783IL_TIMDisconnectFromServer(dbNode client, bytes serverAddress); // form 6
long Iso11783IL_TIMDisconnectFromServer(dbNode client, dbNode server, dword options); // form 7
long Iso11783IL_TIMDisconnectFromServer(dbNode client, bytes serverAddress, dword options); // form 8
```

## Description

Stops TIM connection to a TIM server.

Releases the communication with a connected TIM server.

## Parameters

| Name | Type | Description |
|---|---|---|
| server |  | The client releases the connection to the TIM server specified by this node. |
| serverAddress |  | The client releases the connection to the TIM server with this address. |
| Option | Value | Description |
| Graceful shutdown | 01h | Client gracefully shutdowns connection to the specified server. |
| client |  | TIM client node. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0: form 1, 5 11.0 SP2: form 2, 3, 4, 6, 7, 8 | 13.0 | — | — | 3.0: form 3 3.0 SP2: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 5, 6, 7, 8 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2, 3, 4) | ✔ (form 1, 2, 3, 4) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 5, 6, 7, 8) | ✔ (form 5, 6, 7, 8) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 5, 6, 7, 8) | ✔ (form 5, 6, 7, 8) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
