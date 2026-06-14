# IPRouteAddGateway

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IPRouteAddGateway( dword destination, dword mask, dword gateway); // form 1
long IPRouteAddGateway( byte destination[], dword prefix, byte gateway[]); // form 2
long IPRouteAddGateway( IP_Address destination, dword prefix, IP_Address gateway); // form 3
```

## Description

With this function it is possible to add a static gateway route to the routing table in the tcp/ip stack. Depending on the given mask (IPv4) or prefix (IPv6) a route to a single host or to a network is added (see example).

When such a route is installed the tcp/ip stack will send packets destined to this destination address or network via the given gateway.

## Parameters

| Name | Description |
|---|---|
| destination | The IPv4 or IPv6 destination address of the route. |
| mask | Mask for the given IPv4 address. If an all ones mask is given a gateway route for a single host is installed. Otherwise a network gateway route will be installed . |
| prefix | Prefix for the given IPv6 destination address. If the prefix 128 is given a gateway route for a single host is installed. Otherwise a network gateway route will be installed |
| gateway | The IPv4 or IPv6 Address of the gateway. |

## Example

```c
variables
{
  UdpSocket gSocket;
}

on start
{
  ipRouteAddGateway( IP_Address(192.168.1.0), 24, IP_Address(192.168.0.200) );
  gSocket = UdpSocket::Open( IP_Endpoint(192.168.0.19:40019) );

  // because the destination address of the following send request
  // is in an other sub-net, the UDP packet will be sent to the
  // MAC address of the gateway which was configured above.
  gSocket.SendTo( IP_Endpoint(192.168.1.123:40123), "Hello", 5 );
}

on preStop
{
  ipRouteDeleteGateway( IP_Address(192.168.1.0), 24 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 SP4: form 1-2 12.0: form 3 | 10.0 SP4: form 1-2 12.0: form 3 | 13.0 | 13.0: from 3 | — | 3.0: form 1-2 4.0: form 3 |
| Restricted To | Ethernet | Ethernet | Ethernet | Ethernet | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
