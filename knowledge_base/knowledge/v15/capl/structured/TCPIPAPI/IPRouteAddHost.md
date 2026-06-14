# IPRouteAddHost

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IPRouteAddHost( dword hostAddr, byte macId[] ); // form 1
long IPRouteAddHost( byte hostAddr[], byte macId[] ); // form 2
long IPRouteAddHost( IP_Address hostAddr, qword macId ); // form 3
```

## Description

With this function it is possible to add a static host route to the routing table of a interface in the tcp/ip stack. When such a route is installed the tcp/ip stack will no longer perform a ARP request or neighbor solicitation when a message is sent to this destination.

It is necessary that an interface or network route already exists. So the dedicated interface for this route can be found. When there is no interface route found it is possible to add one with the function IPRouteAddInterface.

## Parameters

| Name | Description |
|---|---|
| hostAddr | The IPv4 or IPv6 destination address of the route |
| macId | The mac ID of the host route |

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
