# SCC_CreateCM_Set_Key_Cnf

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CreateCM_Set_Key_Cnf ( byte SourceMac[], byte TargetMac[], dword Result )
```

## Description

Creates a CM_Set_Key.Cnf message for sending.

## Parameters

| Name | Description |
|---|---|
| SourceMac | Source address of the Ethernet frame. |
| TargetMac | Destination address of the Ethernet frame. |
| Result | Result code: 0x00 = success 0x01 = failure 0x02-0xFF = reserved |
| Index | Name Type Description |
| 0 | MyNonce byte[] 4 byte random number. |
| 1 | YourNonce byte[] Last received nonce (4 byte). |
| 2 | PID dword Protocol ID. |
| 3 | PRN byte[] Protocol Run Number (2 byte). |
| 4 | PMN dword Protocol Message Number. |
| 5 | CCoCapability dword STA’s CCo Capability. |

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
