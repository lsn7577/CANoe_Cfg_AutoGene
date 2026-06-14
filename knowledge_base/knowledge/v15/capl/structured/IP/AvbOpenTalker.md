# AvbOpenTalker

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbOpenTalker( ); // form 1
dword AvbOpenTalker(dword streamUniqueId); // from 2
dword AvbOpenTalker(byte streamSourceAddress[]); // form 3
dword AvbOpenTalker(byte streamSourceAddress[], dword streamUniqueId); // form 4
```

## Description

The function creates a Talker for use in connection-based, message-oriented communications.

## Parameters

| Name | Description |
|---|---|
| streamUniqueId | The stream’s unique identifier. |
| streamSourceAddress | The stream’s source MAC address (6 byte). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP2 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
