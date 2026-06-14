# IPRouteAddGateway

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IPRouteAddGateway( dword destination, dword mask, dword gateway); // form 1
```

## Description

With this function it is possible to add a static gateway route to the routing table in the tcp/ip stack. Depending on the given mask (IPv4) or prefix (IPv6) a route to a single host or to a network is added (see example).

When such a route is installed the tcp/ip stack will send packets destined to this destination address or network via the given gateway.

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

| Since Version |
|---|
