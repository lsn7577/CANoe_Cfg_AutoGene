# CANopenEmergency

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword CANopenEmergency(dword nodeId, dword active, dword errorCode, byte[] specificData, dword dataSize);
```

## Description

Activates/deactivates an emergency error code.

## Parameters

| Name | Description |
|---|---|
| nodeId | CANopen node ID. |
| active | 0: Emergency code deactivated 1: Emergency code activated |
| errorCode | Error code number. |
| specificData | Additional data transmitted with the emergency message. |
| dataSize | Size of specificData. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP2 | 13.0 | — | — | 2.2 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
