# SD_AddProvider

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SD_AddProvider(service svc, char[] name, dword isSimulated, serviceProviderRef * newProvider);
```

## Description

Adds a provider endpoint to a service communication object. The new endpoint may be real and detected through some protocol messages, or it may be simulated to test reaction of a consumer to dynamic endpoint changes.

## Parameters

| Name | Description |
|---|---|
| svc | Service to which the endpoint shall be added. |
| name | Name of the new provider. |
| isSimulated | 1 if the new provider shall be simulated, 0 if it shall be real. |
| newProvider | Receives a reference to the new provider. |

## Example

```c
SD_AddProvider(MirrorAdjustment, "RearMirror", 1, newProvider);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
