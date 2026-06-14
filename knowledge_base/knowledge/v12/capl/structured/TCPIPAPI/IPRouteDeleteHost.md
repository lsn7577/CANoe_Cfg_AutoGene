# IPRouteDeleteHost

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IPRouteDeleteHost( dword hostAddr ); // form 1
```

## Description

With this function it is possible to delete a host route from the routing table of an interface in the tcp/ip stack.

It is necessary that an interface or network route already exists. So the dedicated interface for this route can be found.

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
