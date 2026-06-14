# UdpSendTo

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long UdpSendTo( dword socket, dword address, dword port, char buffer[], dword size); // form 1
socket.SendTo( dword address, dword port, char buffer[], dword size); // form 1
```

## Description

The function sends data to the specified location. If the send operation does not complete immediately the operation is performed asynchronously and the function will return SOCKET_ERROR (-1). Use IpGetLastSocketError to get a more specific error code. If the specific error code is WSA_IO_PENDING (997) and the CAPL callback OnUdpSendTo will be called on completion (successful or not), providing that it is implemented in the same CAPL program.

If the operation has been processed synchronously, the CAPL callback OnUdpSendTo is not called up (see also TcpSend).

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
