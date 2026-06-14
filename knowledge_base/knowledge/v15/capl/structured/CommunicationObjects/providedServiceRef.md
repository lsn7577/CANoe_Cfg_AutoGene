# providedServiceRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
providedServiceRef * <var>; // form 1
providedServiceRef <Service> <var>; // form 2
providedServiceRef <Interface> <var>; // form 3
```

## Description

References a provided service endpoint, which means a specific combination of consumer and provider for a service on provider side.

## Parameters

| Name | Description |
|---|---|
| Service | Service, determining the data type of the object. |
| Interface | Data type of the object (a service interface). |

## Example

```c
providedServiceRef MirrorAdjustment service1;
service1 = MirrorAdjustment.providerSide[CANoe,LeftMirror];
write("State: %d", $service1.ConnectionState);
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
