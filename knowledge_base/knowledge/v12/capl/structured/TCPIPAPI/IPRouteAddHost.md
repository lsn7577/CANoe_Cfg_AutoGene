# IPRouteAddHost

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IPRouteAddHost( dword hostAddr, byte macId[] ); // form 1
```

## Description

With this function it is possible to add a static host route to the routing table of a interface in the tcp/ip stack. When such a route is installed the tcp/ip stack will no longer perform a ARP request or neighbor solicitation when a message is sent to this destination.

It is necessary that an interface or network route already exists. So the dedicated interface for this route can be found. When there is no interface route found it is possible to add one with the function IPRouteAddInterface.

The IP address 192.168.1.1/24 is configured on your network adapter. This means an interface route to the network 192.168.1.00/24 is automatically installed on measurement start. So its possible to add a host route to any address of this network e.g. 192.168.1.10

## Return Values

0: The function completed successfully.

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

| Since Version |
|---|
