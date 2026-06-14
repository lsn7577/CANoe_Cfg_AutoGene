# IPRouteAddInterface

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IPRouteAddInterface( dword destination, dword mask, dword ifIndex); // form 1
long IPRouteAddInterface( byte destination[], dword prefix, dword ifIndex); // form 2
long IPRouteAddInterface(IP_Address destination, dword prefix, dword ifIndex); // form 3
```

## Description

With this function it is possible to add a static route to an interface to the routing table in the tcp/ip stack. Depending on the given mask (IPv4) or prefix (IPv6) a route to a single host or to a network is added (see example).

When such a route is installed the tcp/ip stack will send packets destined to this destination on the given interface.

## Parameters

| Name | Description |
|---|---|
| destination | The IPv4 or IPv6 destination address of the route. |
| mask | Mask for the given IPv4 address. If an all ones mask is given a interface route for a single host is installed. Otherwise a network interface route will be installed. |
| prefix | Prefix for the given IPv6 destination address. If the prefix 128 is given a interface route for a single host is installed. Otherwise a network interface route will be installed. |
| ifIndex | The index of the interface for this route. |

## Example

```c
variables
{
  UdpSocket gSocket;
}

on start
{
  ipRouteAddInterface( IP_Address(192.168.100.0), 24, 2 );
  gSocket = UdpSocket::Open( IP_Endpoint(192.168.0.20:40020) );

  // because the destination address of the following send request
  // is in an other sub-net, the UDP packet will be sent over
  // the interface which was configured above.
  gSocket.SendTo( IP_Endpoint(192.168.100.100:40100), "Hello", 5 );
}

on preStop
{
  ipRouteDeleteInterface( IP_Address(192.168.1.0), 24 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 SP4: form 1-2 12.0: form 3 | 10.0 SP4: form 1-2 12.0: form 3 | 13.0 | 13.0: form 3 | — | 3.0: form 1-2 4.0: form 3 |
| Restricted To | Ethernet | Ethernet | Ethernet | Ethernet | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
