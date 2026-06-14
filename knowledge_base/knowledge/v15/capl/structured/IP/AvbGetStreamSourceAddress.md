# AvbGetStreamSourceAddress

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbGetStreamSourceAddress(dword listenerOrTalkerHandle, byte retStreamSourceAddress[]);
```

## Description

The function retrieves the stream’s Source Address of the Listener or Talker. This usually is a 48 bit MAC address defining the sourcing system of the stream and is part of the Stream Identifier (ID).

## Parameters

| Name | Description |
|---|---|
| listenerOrTalkerHandle | The handle of the Listener or Talker. |
| retStreamSourceAddress | The 48 bit bit Stream Source Address upon successful return of the function. |

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
