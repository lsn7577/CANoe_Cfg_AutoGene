# IPRouteDeleteHost

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IPRouteDeleteHost( dword hostAddr ); // form 1
long IPRouteDeleteHost( byte hostAddr[] ); // form 2
long IPRouteDeleteHost( IP_Address hostAddr ); // form 3
```

## Description

With this function it is possible to delete a host route from the routing table of an interface in the tcp/ip stack.

It is necessary that an interface or network route already exists. So the dedicated interface for this route can be found.

## Parameters

| Name | Description |
|---|---|
| hostAddr | The IPv4 or IPv6 destination address of the route. |

## Example

```c
variables
{
  UdpSocket gSocket;
}

on start
{
  ipRouteAddHost( IP_Address(192.168.0.190), ethGetMacAddressAsNumber("02:00:00:00:00:BE") );
  gSocket = UdpSocket::Open( IP_Endpoint(192.168.0.18:40018) );

  // this send request will send the UDP packet to the MAC address,
  // which was configured above, without performing an ARP request.
  gSocket.SendTo( IP_Endpoint(192.168.0.190:40190), "Hello", 5 );
}

on preStop
{
  ipRouteDeleteHost( IP_Address(192.160.0.190) );
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
