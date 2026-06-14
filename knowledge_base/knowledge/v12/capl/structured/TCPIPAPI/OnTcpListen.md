# OnTcpListen

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnTcpListen( dword socket, long result)
```

## Description

If the CAPL program implements this callback it is called when TcpListen was called and a connection request for the specified socket is received.

The connection must be accepted with TcpAccept because the listen socket otherwise remains blocked for other clients. This block is evident for a client in OnTcpConnect from the output of error code 10061 (Connection refused).

## Return Values

—

## Example

```c
// ---------------------------------------------------
// Callback when client connects to server's listen socket.
// ---------------------------------------------------
void OnTcpListen( dword socket, long result)
{
  dword newSocket;
  newSocket = TcpAccept( socket );
  if (newSocket != ~0)
  {
    // start to receive data on the new socket...
  }
  else
  {
    writeLineEx( 1, 3, "S: TcpAccept: Socket error: %d", IpGetLastSocketError (socket) );
  }
}
```

## Availability

| Since Version |
|---|
