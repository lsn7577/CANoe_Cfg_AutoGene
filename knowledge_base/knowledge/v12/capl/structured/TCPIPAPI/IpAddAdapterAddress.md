# IpAddAdapterAddress

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpAddAdapterAddress(dword ifIndex, dword ipv4address, dword ipv4mask);
```

## Description

The function adds an address to the network interface with the given index.

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
  ipAddAdapterAddress( 1, IP_Address( 192.168.0.116 ), 24 );
  gSocket = UdpSocket::Open( IP_Endpoint(192.168.0.116:40016) );
  gSocket.SendTo( IP_Endpoint(192.168.0.255:40255), "Hello", 5 );
}

on preStop
{
  ipRemoveAdapterAddress( 1, IP_Address( 192.168.0.116 ), 24 );
}
```

## Availability

| Since Version |
|---|
