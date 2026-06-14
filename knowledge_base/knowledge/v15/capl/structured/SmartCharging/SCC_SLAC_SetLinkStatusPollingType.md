# SCC_SLAC_SetLinkStatusPollingType

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SLAC_SetLinkStatusPollingType ( dword Type )
```

## Description

Changes the message(s) used for querying the link status (if activated). This overwrites the configuration parameter <SLAC_LinkStatusPollingType>.

## Parameters

| Name | Description |
|---|---|
| Type | Desired message configuration, where the following applies: 0 = use both available messages 1 = use only VS_PL_Lnk_Status 2 = use only VS_Nw_Info |

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
