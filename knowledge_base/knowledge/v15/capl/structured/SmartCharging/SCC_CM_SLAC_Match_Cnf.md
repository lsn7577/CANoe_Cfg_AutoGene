# SCC_CM_SLAC_Match_Cnf

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CM_SLAC_Match_Cnf ( byte RunId[], byte SourceMacAddress[], byte PEVMAC[], byte EVSEMAC[], byte NID[], byte NMK[] )
```

## Description

The callback is called as soon as a CM_SLAC_Match.Cnf message is received. Further details that are transmitted in this request can be queried with the following functions:

## Parameters

| Name | Description |
|---|---|
| RunId | Random Run Identifier of sender (8 byte). |
| SourceMacAddress | MAC address of sender. |
| PEVMAC | PEV MAC Address. |
| EVSEMAC | EVSE MAC Address. |
| NID | Network ID given by the CCo (EVSE). |
| NMK | Private NMK of the EVSE (random value). |

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
