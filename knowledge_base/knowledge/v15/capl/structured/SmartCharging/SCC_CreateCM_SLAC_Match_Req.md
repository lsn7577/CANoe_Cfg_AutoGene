# SCC_CreateCM_SLAC_Match_Req

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CreateCM_SLAC_Match_Req ( byte RunId[], byte SourceMac[], byte TargetMac[], byte PEVMacAddress[], byte EVSEMacAddress[] )
```

## Description

Creates a CM_SLAC_Match.Req message for sending.

## Parameters

| Name | Description |
|---|---|
| RunId | Random Run Identifier of sender (8 byte). |
| SourceMac | Source address of the Ethernet frame. |
| TargetMac | Destination address of the Ethernet frame. |
| PEVMacAddress | MAC Address of the PEV. |
| EVSEMacAddress | MAC Address of the EVSE. |
| Index | Name Type Description |
| 0 | ApplicationType dword 0x00 = PEV-EVSE Association 0x01-0xFF = Reserved |
| 1 | SecurityType dword 0x00 = No Security 0x01 = Public Key Signature 0x02-0xFF = Reserved |
| 2 | MVFLength dword Length of the match variable field. |
| 3 | PEVID byte[] 17 byte ID |
| 4 | EVSEID byte[] 17 byte ID |
| 5 | Reserved field byte[] 8 byte |

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
