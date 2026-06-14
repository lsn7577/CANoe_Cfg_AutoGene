# SCC_MessageRxInd

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_MessageRxInd(byte SessionID[], dword MessageID)
```

## Description

The callback is called each time a Vehicle2Grid, SECC Discovery or SLAC message is received by the simulation DLL.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of the connection, range: 0 - 0xFF FF FF FF FF FF FF FF |
| MessageID | Type of received message: For SLAC messages, MMType (2 byte) according to specification. For V2G messages see help page MessageID. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP2 | — | — | — | 3.0 SP3 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
