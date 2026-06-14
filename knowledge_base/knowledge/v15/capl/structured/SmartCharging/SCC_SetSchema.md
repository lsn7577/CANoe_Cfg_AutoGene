# SCC_SetSchema

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_SetSchema ( char Namespace[] )
void SCC_SetSchema ( char Namespace[], long VersionMajor, long VersionMinor )
```

## Description

Sets the preferred schema version, corresponding to <SchemaNamespace> and optionally a specific version, in the XML configuration file.

The configured schema will be used unless a different one is derived from the SupportedAppProtocol handshake, and it will be prioritized during the handshake. If unspecified, the latest schema will have the highest priority.

When no version numbers are specified, depending on the context, it will mean any or latest version.

## Parameters

| Name | Description |
|---|---|
| SchemaNamespace | Desired namespace. |
| SchemaVersionMajor | Desired major version number, may be -1 for EVSE simulation. |
| SchemaVersionMinor | Desired minor version number, may be -1 for EVSE simulation. |

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
