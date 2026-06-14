# SD_ConnectAsync

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void SD_ConnectAsync(providedServiceRef * providedService); // form 1
void SD_ConnectAsync(consumedServiceRef * consumedService); // form 2
```

## Description

Requests that a connection will be established between a service provider and a service consumer. The connection will be established asynchronously, i.e. after the call it will in the general case not be available immediately. You can react to the establishment of the connection with an on SD_connection_established (or on SD_connection_failed) handler. You can call the function from both the provider and the consumer side.

Note that you need this function only when you implement service discovery yourself. In most cases, there’s an internal CANoe model for simulated endpoints which handles the protocol.

## Parameters

| Name | Description |
|---|---|
| providedService | Endpoints, from provider side. |
| consumedService | Endpoints, from consumer side. |

## Return Values

—

## Example

```c
SD_ConnectAsync(consumedService);
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
