# SCC_CM_Validate_Cnf

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CM_Validate_Cnf ( byte RunId[], byte SourceMacAddress[], dword Result, dword ToggleNum )
```

## Description

The callback is called as soon as a CM_Validate.Cnf message is received. Further details (signal type) that are transmitted in this request can be queried with SCC_SLAC_GetSignalType.

## Parameters

| Name | Description |
|---|---|
| RunId | Random Run Identifier of sender (8 byte). |
| SourceMacAddress | MAC address of sender. |
| SourceAddress | MAC Address of the EV which initiates the SLAC process. |
| NumSounds | Number of M-Sounds used to generate the ATTEN_PROFILE. |
| NumGroups | Number of attenuation groups. |
| AAG | Average Attenuation Group (array length is indicated by the parameter NumGroups). |

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
