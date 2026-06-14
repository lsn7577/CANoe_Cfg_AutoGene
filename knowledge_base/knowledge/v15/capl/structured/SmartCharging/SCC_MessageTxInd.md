# SCC_MessageTxInd

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_MessageTxInd ( byte SessionOrRunID[], dword MessageID, long Error )
```

## Description

The callback is called each time a Vehicle2Grid, SECC Discovery or SLAC message is sent by the simulation DLL.

## Parameters

| Name | Description |
|---|---|
| SessionOrRunID | 8-byte long SessionID (V2G) or RunID (SLAC) of the connection, range: 0 – 0xFF FF FF FF FF FF FF FF. |
| MessageID | Type of sent message: For SLAC messages, MMType (2 byte) according to specification. For V2G messages see help page MessageID. |
| Error | 0 if the sending was successful. > 0 if the send call failed (sending may fail due to socket errors or the absence of a receiver which sends ACK packages). |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | 3.0 SP3 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
