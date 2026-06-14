# IpBind

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpBind( dword socket, dword address, dword port); // form 1
long IpBind( dword socket, byte ipv6Address[], dword port); // form 2
long IpBind( dword socket, IP_Endpoint localEndpoint ); // form 3
```

## Description

The function associates an address and a port with the specified socket, after an unbound socket has been generated with TcpOpen(0, 0).

Do not use IpBind when you are working with TcpConnect or TcpListen because these two commands bind the socket implicitly.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle of the socket to be bound. |
| address | The numerical local IPv4 address. |
| ipv6address | The local IPv6 address in a 16 byte array. |
| port | The local port in host-byte order. |
| localEndpoint | Bind the socket to this local endpoint. IP Address can be 0, if the socket should not be bound to an address. Port number can be undefined, if a dynamic port number should be used. Examples: IP_Endpoint(192.168.1.1:4000) – Bind to address and port IP_Endpoint(0.0.0.0:4000) – Bind only to port for IPv4 IP_Endpoint([::]:4000) – Bind only to port for IPv6 IP_Endpoint(192.168.1.1) – Bind to address and choose a dynamic port |

## Example

```c
variables
{
  UdpSocket gSocket;
  char gRxBuffer[1000];
}

on start
{
  gSocket = UdpSocket::Open( IP_Endpoint(0.0.0.0) );
}

on key '1'
{
  gSocket.Bind( IP_Endpoint(192.168.0.7:40007) );
  gSocket.SendTo( IP_Endpoint(192.168.0.100:40100), "Hello", 5 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: function/method 1-2 12.0: function/method 3 | 7.0: function 1-2 7.0 SP5: method 1-2 12.0: function /method 3 | 13.0 | 13.0: form 3 | — | 2.0 SP2: function/method 1-2 4.0: function/method 3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
