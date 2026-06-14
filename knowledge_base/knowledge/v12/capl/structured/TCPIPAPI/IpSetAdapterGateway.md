# IpSetAdapterGateway

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpSetAdapterGateway (dword ifIndex, dword ipv4address); // form 1
```

## Description

The function sets the default gateway address. There can only be one default gateway. An old default gateway address will be overwritten. The default gateway has to be in one of the subnets configured in the network stack, otherwise the network stack will not be able to find a route to the gateway. To remove the gateway, set the address 0.0.0.0 (IPv4) or :: (IPv6).

The function is dependent on the selected stack.

This functionality cannot be used in connection with the operating system TCP/IP stack.

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
  ipSetAdapterGateway( 1, IP_Address(192.168.0.200) );
  gSocket = UdpSocket::Open( IP_Endpoint(192.168.0.17:40017) );

  // this send call to another sub-net will request the MAC address
  // of the gateway and sent the UDP packet to the MAC address of the gateway.
  gSocket.SendTo( IP_Endpoint(192.168.1.100:40100), "Hello", 5 );
}
```

## Availability

| Since Version |
|---|
