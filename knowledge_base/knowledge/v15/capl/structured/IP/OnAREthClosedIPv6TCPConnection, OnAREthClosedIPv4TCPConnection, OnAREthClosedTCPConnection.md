# OnAREthClosedIPv6TCPConnection, OnAREthClosedIPv4TCPConnection, OnAREthClosedTCPConnection

> Category: `IP` | Type: `function`

## Syntax

```c
void OnAREthClosedIPv6TCPConnection(byte localIPv6Address[], dword localPort, byte remoteIPv6Address[], dword remotePort); // form 1
void OnAREthClosedIPv4TCPConnection(dword localIPv4Address, dword localPort, dword remoteIPv4Address, dword remotePort); // form 2
void OnAREthClosedTCPConnection(IP_Endpoint localIPEndpoint, IP_Endpoint remoteIPEndpoint); // form 3
```

## Description

This callback will be called after a IL’s TCP connection has been closed.

## Parameters

| Name | Description |
|---|---|
| localIPv6Address | Local IPv6 address. |
| remoteIPv6Address | Remote IPv6 address. |
| localIPv4Address | Local IPv4 address. |
| remoteIPv4Address | Remote IPv4 address. |
| localPort | Local TCP port number. |
| remotePort | Remote TCP port number. |
| localIPEndpoint | Object of type IP_Endpoint that contains the address/port of the local endpoint. |
| remoteIPEndpoint | Object of type IP_Endpoint that contains the address/port of the remote endpoint. |

## Example

```c
void OnAREthClosedTCPConnection(IP_Endpoint localIPEndpoint, IP_Endpoint remoteIPEndpoint)
{
  char localEndpointStr[128], remoteEndpointStr[128];

  localIPEndpoint.PrintEndpointToString(localEndpointStr);
  remoteIPEndpoint.PrintEndpointToString(remoteEndpointStr);

  write("Closed connection: %s <-> %s", localEndpointStr,  remoteEndpointStr);
}
```

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
