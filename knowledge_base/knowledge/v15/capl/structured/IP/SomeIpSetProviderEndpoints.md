# SomeIpSetProviderEndpoints

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSetProviderEndpoints(dword csiHandle, dword remoteIPv4Address, dword remoteUDPPort, dword remoteTCPPort); // form 1
long SomeIpSetProviderEndpoints(dword csiHandle, byte remoteIPv6Address[], dword remoteUDPPort, dword remoteTCPPort); // form 2
long SomeIpSetProviderEndpoints(dword csiHandle, IP_Endpoint remoteIPEndpoint); // form 3
```

## Description

Sets the UDP and TCP endpoint that is used for the consumed service instance to reach the corresponding provided service instance.

## Parameters

| Name | Description |
|---|---|
| csiHandle | Consumed service instance handle (may be retrieved by SomeIpGetConsumedObjectHandle). |
| remoteIPv4Address | IPv4 address of the provider. In network byte order. |
| remoteIPv6Address | IPv6 address of the provider. |
| remoteUDPPort | An UDP port number of the provideror zero if there is none. |
| remoteTCPPort | A TCP port number of the provideror zero if there is none. |
| remoteIPEndpoint | Object of type IP_Endpoint that contains the address/port of the provider. An IP_Endpoint with port number zero may be passed to delete a previously set IP_Endpoint. |

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
