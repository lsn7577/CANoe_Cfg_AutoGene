# AvbGetProtocol

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbGetProtocol(dword listenerOrTalkerHandle, dword& retProtocol);
```

## Description

The function retrieves the AVTP protocol of the Listener or Talker.

## Parameters

| Name | Description |
|---|---|
| listenerOrTalkerHandle | The handle of the Listener or Talker. |
| Value | Name |
| 0x02 | AAF (AVTP Audio Format) |
| 0x04 | CRF (Clock Reference Format) |

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
