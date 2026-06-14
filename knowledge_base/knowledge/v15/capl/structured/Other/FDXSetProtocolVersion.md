# FDXSetProtocolVersion

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXSetProtocolVersion(long fdxClientHandle, byte majorVersion, byte minorVersion);
```

## Description

This function configures the version of the FDX protocol that should be used for the communication with the specified client.

## Parameters

| Name | Description |
|---|---|
| fdxClientHandle | FDX client for which the protocol version should be set. |
| majorVersion | Major version of the FDX protocol |
| minorVersion | Minor version of the FDX protocol |

## Example

See also: Coupling of two CANoe Instances using the FDX Protocol

```c
// Configure FDX protocol version 1.2 for the given client
FDXSetProtocolVersion(fdxClientHandle, 1, 2);

// Configure FDX protocol version 2.0 for the given client
FDXSetProtocolVersion(fdxClientHandle, 2, 0);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 | 13.0 | — | 14 | 2.2 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
