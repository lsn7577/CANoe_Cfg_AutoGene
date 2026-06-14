# SCC_InvalidMessageInd

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_InvalidMessageInd ( long MessageType, long ErrorCode )
```

## Description

The callback is called when a SDP or V2G message is received with an invalid content (i.e. it is rejected by the session layer).

## Parameters

| Name | Description |
|---|---|
| MessageType | Type of the invalid message: 0: SDP (SECC Discovery Protocol) 1: V2G (Vehicle2Grid) |
| ErrorCode | Type of error: 0: Wrong version number, or version number format 1: Unknown payload type 2: Invalid payload length 3: Error while decoding (EXI or XML parsing failed) – V2G only 4: Invalid signature – V2G only |

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
