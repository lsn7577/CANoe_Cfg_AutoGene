# TCPGetRemoteAddress

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword TcpGetRemoteAddress(dword socket); // form 1
dword TCPGetRemoteAddress(dword socket, byte remoteIpv6Address[]); // form 2
long TcpGetRemoteAddress(dword socket, IP_Address &address): // form 3
```

## Description

This function retrieves the remote IPv4 address of the specified connected socket.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| remoteIpv6Address | The container for the remote IPv6 address in a 16 byte array. |
| address | IP_Address which returns the IP address. |

## Return Values

The IPv4 address of the remote host in network-byte order.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: form 1-2 12.0: form 3 | 7.2: form 1-2 12.0: form 3 | 13.0 | 13.0: form 3 | — | 2.0 SP2: form 1-2 4.0: form 3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
