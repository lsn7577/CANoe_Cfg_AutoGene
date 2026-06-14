# SomeIpEstablishTCPConnection

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpEstablishTCPConnection (); // form 1
dword SomeIpEstablishTCPConnection (dword aepHandle); // form 2
dword SomeIpEstablishTCPConnection (dword aepHandle, dword remoteIPv4Address); // form 3
dword SomeIpEstablishTCPConnection (dword aepHandle, dword remoteIPv4Address, dword remotePort); // form 4
dword SomeIpEstablishTCPConnection (dword aepHandle, byte remoteIPv6Address[]); // form 5
long SomeIpEstablishTCPConnection (dword aepHandle, byte remoteIPv6Address[], dword remotePort); // form 6
long SomeIpEstablishTCPConnection (dword aepHandle, IP_Endpoint remoteIPEndpoint); // form 7
```

## Description

Establishes one or multiple database defined TCP connection(s).

A TCP connection can be closed using the SomeIpCloseEstablishedTCPConnection function.

## Parameters

| Name | Description |
|---|---|
| aepHandle | Source application endpoint, which initiates the connection(s).Has to be defined in the database. |
| remotePort | Port on which the messages can be both sent and received. |
| remoteIPv4Address | IPv4 address to which the connection should be etablished. IPv4 address can be converted with IPGetAdressAsNumber. |
| remoteIPv6Address | IPv6 address to which the connection should be etablished. IPv6 address can be converted with IpGetAddressAsArray. |
| remoteIPEndpoint | Object of type IP_Endpoint that contains the address/port of the remote endpoint. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3: form 1-6 12.0 SP2: form 7 | — | — | — | 3.1: form 1-6 4.0 SP2: form 7 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
