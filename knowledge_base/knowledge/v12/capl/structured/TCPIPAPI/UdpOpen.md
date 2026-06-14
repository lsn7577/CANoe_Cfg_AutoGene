# UdpOpen

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword UdpOpen( dword ipv4Address, dword port); // form 1
```

## Description

Depending on the address type, the function creates either an IPv4 or IPv6 UDP socket for use in connectionless, datagramm-oriented communications. All parameters may be zero. If the port parameter is non-zero, the socket is implicitly bound to the given port. Otherwise the socket can be bound later on with IpBind or it will be automatically bound to a free port with UdpSendTo.

Note:

If an address is given but the port is zero, no implicit bind is performed. Please use IpBind after opening the socket in this case.

## Return Values

INVALID_SOCKET (~0): The function failed. Call IpGetLastError to get a more specific error code.

## Example

```c
variables
{
  UdpSocket gSocket;
  char      gRxBuffer[1000];
}

on start
{
  gSocket = UdpSocket::Open( IP_Endpoint(0.0.0.0:40001) );
  gSocket.SendTo( IP_Endpoint(192.168.0.2:40002), "Hello", 5 );
  gSocket.ReceiveFrom( gRxBuffer, elcount( gRxBuffer) );
}

OnUdpReceiveFrom( UdpSocket socket, long result, IP_Endpoint remoteEndpoint, char buffer[], dword size)
{
  if (result == 0)
  {
    write( "Received: %s", buffer );
    gSocket.ReceiveFrom( gRxBuffer, elcount( gRxBuffer) );
  }
}
```

## Availability

| Since Version |
|---|
