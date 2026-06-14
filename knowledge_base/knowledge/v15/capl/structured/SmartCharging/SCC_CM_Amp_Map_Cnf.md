# SCC_CM_Amp_Map_Cnf

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CM_Amp_Map_Cnf(byte RunID[], byte SourceMac[], dword ResType)
```

## Description

The callback is called as soon as a CM_Amp_Map.Cnf message is received.

## Parameters

| Name | Description |
|---|---|
| RunID | 8-byte long run ID |
| SourceMac | MAC address of sender |
| ResType | 0x00 = Success 0x01 = Failure |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP4 | — | — | — | 3.0 SP3 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
