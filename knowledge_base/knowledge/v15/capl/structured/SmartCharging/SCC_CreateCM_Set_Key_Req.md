# SCC_CreateCM_Set_Key_Req

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CreateCM_Set_Key_Req ( byte SourceMac[], byte TargetMac[], byte NID[], byte NMK[] )
```

## Description

Creates a CM_Set_Key.Req message for sending.

## Parameters

| Name | Description |
|---|---|
| SourceMac | Source address of the Ethernet frame. |
| TargetMac | Destination address of the Ethernet frame. |
| NID | Network ID given by the CCo (EVSE) (7 byte). |
| NMK | NMK to be set (16 byte). |
| Index | Name Type Description |
| 0 | KeyType dword 0x00 = DAK (AES-128) 0x01 = NMK (AES-128) 0x02 = NEK (AES-128) 0x03 = TEK (AES-128) 0x04 = Hash Key (Random-3072) 0x05 = Nonce Only (no key) 0x06-0xFF = Reserved |
| 1 | MyNonce byte[] 4 byte random number. |
| 2 | YourNonce byte[] Last received nonce (4 byte). |
| 3 | PID dword Protocol ID. |
| 4 | PRN byte[] Protocol Run Number (2 byte). |
| 5 | PMN dword Protocol Message Number. |
| 6 | CCoCapability dword STA’s CCo Capability. |
| 7 | NewEKS dword PEKS or EKS. |

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
