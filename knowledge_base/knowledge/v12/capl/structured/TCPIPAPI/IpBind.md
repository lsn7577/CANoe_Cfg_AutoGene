# IpBind

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpBind( dword socket, dword address, dword port); // form 1
socket.Bind( dword address, dword port); // form 1
```

## Description

The function associates an address and a port with the specified socket, after an unbound socket has been generated with TcpOpen(0, 0).

Do not use IpBind when you are working with TcpConnect or TcpListen because these two commands bind the socket implicitly.

## Return Values

0: The function completed successfully.

## Example

```c
variables
{
  UdpSocket gSocket;
  char gRxBuffer[1000];
}

on start
{
  gSocket = UdpSocket::Open( IP_Endpoint(0.0.0.0) );
}

on key '1'
{
  gSocket.Bind( IP_Endpoint(192.168.0.7:40007) );
  gSocket.SendTo( IP_Endpoint(192.168.0.100:40100), "Hello", 5 );
}
```

## Availability

| Since Version |
|---|
