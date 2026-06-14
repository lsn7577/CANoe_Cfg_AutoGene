# Abstract_CreateAddress

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
addressHandle Abstract_CreateAddress(CommunicationObject co, char[] name);
```

## Description

Creates a pseudo address for a communication object endpoint if abstract binding is used. The address can be attached to an endpoint with SD_SetAddress. For abstract binding, the address of an endpoint actually does not contain more information than a name which can be retrieved again through Abstract_GetDisplayName.

The address is necessary for implementation of service discovery; e.g. in the handlers on SD_consumer_discovered and on SD_provider_discovered, the address is passed as a selector.

## Parameters

| Name | Description |
|---|---|
| co | Communication object (usually a service) for which the address shall be created. |
| name | Name for the address (e.g. the name of the endpoint). |

## Return Values

—

## Example

```c
SD_SetAddress(newProvider, Abstract_CreateAddress(MirrorAdjustment, "RearMirror"), MirrorAdjustment[CANoe]);
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
