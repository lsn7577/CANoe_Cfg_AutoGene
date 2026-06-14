# SCC_CreateVS_PL_Lnk_Status_Cnf

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CreateVS_PL_Lnk_Status_Cnf ( byte SourceMac[], byte TargetMac[], dword MStatus, dword LinkStatus )
```

## Description

Creates a VS_PL_Lnk_Status.Cnf message for sending.

## Parameters

| Name | Description |
|---|---|
| SourceMac | Source address of the Ethernet frame. |
| TargetMac | Destination address of the Ethernet frame. |
| MStatus | MME Status: 0x00 = success 0xFF = failure |
| LinkStatus | Indicates if a link is established: 0x00 = no link 0x01 = link |
| Index | Name Type Description |
| 0 | OUI byte[] 3 byte Organizationally Unique Identifier. |

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
