# OnUdpReceiveFrom

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnUdpReceiveFrom( dword socket, long result, dword address, dword port, char buffer[], dword size); // form 1
```

## Description

If the CAPL program implements this callback it is called when an asynchronous receive operation on an UDP socket completes.

The stack contains a data queue that is reduced by UdpReceiveFrom as soon as data are located there.

So that additional data from the data queue will be received in the future for the socket, UdpReceiveFrom must be called up again within the callback.

## Return Values

—

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
