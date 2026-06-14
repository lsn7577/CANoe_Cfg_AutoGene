# SCC_SLACFinishedInd

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_SLACFinishedInd ( dword Result )
```

## Description

The callback is called when a SLAC run has been completed. It marks the point in time when the SECC Discovery process can be started, if a match has been found and as soon as the link is established.

The vehicle can use the function SCC_SLAC_GetAttenResults during this callback to get the measured attenuation values.

## Parameters

| Name | Description |
|---|---|
| Result | Result of the SLAC run (2 = PLC link established and interval for Amplitude Map Exchange elapsed,1 = match, 0 = no match). |

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
