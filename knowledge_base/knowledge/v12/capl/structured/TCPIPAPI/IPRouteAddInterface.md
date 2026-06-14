# IPRouteAddInterface

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IPRouteAddInterface( dword destination, dword mask, dword ifIndex); // form 1
```

## Description

With this function it is possible to add a static route to an interface to the routing table in the tcp/ip stack. Depending on the given mask (IPv4) or prefix (IPv6) a route to a single host or to a network is added (see example).

When such a route is installed the tcp/ip stack will send packets destined to this destination on the given interface.

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

| Since Version |
|---|
