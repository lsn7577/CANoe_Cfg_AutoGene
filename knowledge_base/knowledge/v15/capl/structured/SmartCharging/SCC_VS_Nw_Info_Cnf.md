# SCC_VS_Nw_Info_Cnf

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_VS_Nw_Info_Cnf ( byte SourceMacAddress[], long NumAvLn, byte NID[] )
```

## Description

The callback is called as soon as a VS_Nw_Info.Cnf message is received. This is a response of the QCA7000 chip when using link status polling. (Additional data cannot be queried at the moment.)

## Parameters

| Name | Description |
|---|---|
| SourceMacAddress | MAC address of sender. |
| NumAvLn | Number of AVLANs (> 0 denotes an established link). |
| NID | Network ID (7 byte). |

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
