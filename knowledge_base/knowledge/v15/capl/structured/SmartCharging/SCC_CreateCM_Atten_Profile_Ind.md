# SCC_CreateCM_Atten_Profile_Ind

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CreateCM_Atten_Profile_Ind ( byte SourceMac[], byte TargetMac[], byte PEVMAC[], dword NumGroups, byte AAG[] )
```

## Description

Creates a CM_Atten_Profile.Ind message for sending.

## Parameters

| Name | Description |
|---|---|
| SourceMac | Source address of the Ethernet frame. |
| TargetMac | Destination address of the Ethernet frame. |
| PEVMAC | PEV MAC Address. |
| NumGroups | Number of attenuation groups. |
| AAG | Average Attenuation Group (array length is indicated by the parameter NumGroups). |
| Index | Name Type Description |
| 0 | Reserved field dword 1 byte |

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
