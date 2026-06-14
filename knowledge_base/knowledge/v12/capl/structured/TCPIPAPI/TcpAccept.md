# TcpAccept

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword TcpAccept( dword socket);
```

## Description

The function accepts an incoming connection request on the specified socket resulting in a new socket . If the operation fails, the function will return INVALID_SOCKET (~0).

A listen socket created with TcpListen is responded to with callback function OnTcpListen when the connection is established by a client with TcpConnect.

The incoming connection must always be accepted with TcpAccept. That is typically carried out in callback function OnTcpListen.

As long as the connection is not accepted, no other clients can be accepted on the listen socket. All other incoming clients then have error 10061 (Connection refused) delivered in callback OnTcpConnect and can also no longer be accepted subsequently.

Without acceptance of the connection the system goes to a state in which nothing else happens because no data can be sent and other clients are refused on the listen socket.

There is a queue size for incoming connections in the stack. This is set permanently to 1 in CANoe so that only one client can be in the queue until it is accepted.

As soon as the connection has been accepted, there is a new socket for the client on which incoming data can be awaited with TcpReceive and on which data can be sent to the client with TcpSend.

## Return Values

INVALID_SOCKET (~0): The function failed. Call IpGetLastError to get a more specific error code. If this error code is WSA_INVALID_PARAMETER (87), the specified socket was invalid. Otherwise use IpGetLastSocketError to get the reason for the failing.

## Example

```c
// ---------------------------------------------------
// Callback when client connects to server's listen socket.
// ---------------------------------------------------
void OnTcpListen( dword socket, long result)
{
  dword newSocket;
  newSocket = TcpAccept( socket );
  if (newSocket != INVALID_SOCKET)
  {
    // start to receive data on newSocket with TcpReceive...
  }
  else
  {
    writeLineEx( 1, 3, "TcpAccept: Error %d", IpGetLastSocketError(listenSocket));
  }
}
```

## Availability

| Since Version |
|---|
