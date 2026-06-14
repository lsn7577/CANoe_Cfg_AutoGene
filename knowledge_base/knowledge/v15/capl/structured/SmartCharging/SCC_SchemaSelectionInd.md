# SCC_SchemaSelectionInd

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_SchemaSelectionInd ( char Namespace[], dword VersionMajor, dword VersionMinor )
```

## Description

Indicates that a schema has been chosen via the SupportedAppProtoco handshake.

(The EVSE simulation automatically chooses a protocol from the vehicle’s list based on the priority.)

## Parameters

| Name | Description |
|---|---|
| Namespace | Namespace string of the selected schema. |
| VersionMajor | Major version of the selected schema. |
| VersionMinor | Major version of the selected schema. |

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
