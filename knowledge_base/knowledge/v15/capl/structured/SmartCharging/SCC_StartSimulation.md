# SCC_StartSimulation

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_StartSimulation ( ) // form 1
long SCC_StartSimulation ( dword SLACMode ) // form 2
```

## Description

These functions start the simulation DLL in active mode.

With the vehicle DLL, the call of SCC_StartSimulation() starts the setup of a connection.

## Parameters

| Name | Description |
|---|---|
| SLACMode | Controls the behavior regarding SLAC, which overrides the parameter <UseSLAC> from the XML configuration: 0 = SLAC is skipped (may be done manually) 1 = SLAC is used 2 = EV: use SLAC depending on link status (not recommended due to HomePlug Green PHY chip instabilities) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3: form 1, 2 | — | — | — | 3.0 SP3: form 1, 2 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
