# SCC_CreateCM_Amp_Map_Req

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CreateCM_Amp_Map_Req ( byte SourceMac[], byte TargetMac[], dword AmLen, byte AmData[] )
```

## Description

Creates a CM_Amp_Map.Req message for sending.

## Parameters

| Name | Description |
|---|---|
| SourceMac | Source address of the Ethernet frame. |
| TargetMac | Destination address of the Ethernet frame. |
| AmLen | Length of the AmData array. |
| AmData | Power spectral density difference values as defined by the specification Note: Because the PSD is defined in values of 4 bit, only the lower half of each byte is considered. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | — | — | — | 4.0 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
