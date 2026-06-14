# SD_SetAddress

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SD_SetAddress(serviceConsumerRef * consumer, addressHandle address, serviceConsumerRef * simulatedEndpoint); // from 1
long SD_SetAddress(serviceConsumerRef * consumer, addressHandle address, serviceProviderRef * simulatedEndpoint); // from 2
long SD_SetAddress(serviceProviderRef * provider, addressHandle address, serviceConsumerRef * simulatedEndpoint); // from 3
long SD_SetAddress(serviceProviderRef * provider, addressHandle address, serviceProviderRef * simulatedEndpoint); // from 4
```

## Description

Sets the address for an endpoint, normally after it has been added dynamically to a service. The address can be created with binding specific functions. The third parameter is the simulated endpoint where the new endpoint has been discovered and where the address for the new endpoint is now known.

## Parameters

| Name | Description |
|---|---|
| consumer | Consumer endpoint of which the address shall be set. |
| provider | Provider endpoint of which the address shall be set. |
| address | Address for the endpoint. |
| simulatedEndpoint | Endpoint from which the function is called. |

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
