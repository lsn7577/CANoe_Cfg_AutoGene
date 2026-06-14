# SD_AnnounceProvider

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SD_AnnounceProvider(serviceProviderRef * provider); // form 1
void SD_AnnounceProvider(providedServiceRef * providedService); // form 2
```

## Description

Announces over the network that a service provider is running. You can pass either a provider endpoint, which will announce it generally (to a service registry or to all known consumers or by broadcast, depending on the binding protocol). Or you can pass a specific endpoint combination, which will announce it only to the given consumer endpoint.

Note that the provider will be automatically announced if you call ProvideService on the endpoint.

## Parameters

| Name | Description |
|---|---|
| provider | provider endpoint. |
| providedService | Service provided by an endpoint for a consumer. |

## Example

```c
SD_AnnounceProvider(newProvider);
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
