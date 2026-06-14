# SCC_CreateCM_Validate_Req

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CreateCM_Validate_Req ( byte SourceMac[], byte TargetMac[], dword ListenTimer )
```

## Description

Creates a CM_Validate.Req message for sending.

## Parameters

| Name | Description |
|---|---|
| SourceMac | Source address of the Ethernet frame. |
| TargetMac | Destination address of the Ethernet frame. |
| ListenTimer | Time duration while the EVSE shall listen to BCB-toggles: 0x00 = 100 ms 0x01 = 200 ms |
| Index | Name Type Description |
| 0 | SignalType dword 0x00 = PEV S2 toggles on CPLT line 0x01-0xFF = Reserved |
| 1 | Result dword 0x00 = Not Ready 0x01 = Ready 0x02 = Success 0x03 = Failure 0x04 = Not Required 0x05-0xFF = Reserved |

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
