# SomeIpProvidedFieldAddConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpProvidedFieldAddConsumer(dword pfHandle, dword remoteIPv4Address, dword remoteUDPPort, dword remoteTCPPort); // form 1
long SomeIpProvidedFieldAddConsumer(dword pfHandle, byte remoteIPv6Address[], dword remoteUDPPort, dword remoteTCPPort); // form 2
long SomeIpProvidedFieldAddConsumer(dword pfHandle, IP_Endpoint remoteIPEndpoint); // form 3
```

## Description

Adds a consumer to a provided field. Afterwards the field notifications will be sent to this consumer.

## Parameters

| Name | Description |
|---|---|
| pfHandle | Provided field handle (may be retrieved by SomeIpGetProvidedObjectHandle) |
| remoteIPv4Address | IPv4 address of the consumer. In network byte order. |
| remoteIPv6Address | IPv6 address of the consumer |
| remoteUDPPort | An UDP port number of the consumer or zero if there is none |
| remoteTCPPort | A TCP port number of the consumer or zero if there is none |
| remoteIPEndpoint | Object of type IP_Endpoint that contains the address/port of the consumer. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3: form 1-2 12.0 SP2: form 3 | — | — | — | 3.0 SP3: form 1-2 4.0 SP2: form 3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
