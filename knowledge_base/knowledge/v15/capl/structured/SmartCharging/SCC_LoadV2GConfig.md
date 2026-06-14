# SCC_LoadV2GConfig

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_LoadV2GConfig ( long ConfigID )
```

## Description

Loads the section within the XML configuration file designated with configID. If LoadCommunicationConfig has not yet been called when the simulation starts, section 0 is loaded automatically.

The function SCC_LoadCommunicationConfig loads the configuration globally, i.e. for all connections to be created. This call is only possible when simulation is deactivated.

The function SCC_LoadV2GConfig loads the configuration for an already active connection, applying only those parameters relevant to an individual connection.

## Parameters

| Name | Description |
|---|---|
| ConfigID | ID of desired configuration section. |

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
