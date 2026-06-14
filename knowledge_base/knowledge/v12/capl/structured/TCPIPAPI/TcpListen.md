# TcpListen

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long TcpListen( dword socket);
socket.Listen();
```

## Description

The function causes the socket to listen for incoming connection requests, which will be provided in the CAPL callback OnTcpListen, if it is implemented in the same CAPL program. If the operation fails, the function will return SOCKET_ERROR (-1). Use IpGetLastSocketError to get a more specific error code.

The socket must have been opened beforehand with TcpOpen and be bound at least to one port. The binding to the port is carried out during opening or using IpBind.

The additional binding to an IP address is optional.

Incoming connections on the listen socket must be accepted with TcpAccept because all other connections will otherwise be refused with error 10061 (Connection refused).

## Return Values

0: The function completed successfully.

## Example

```c
// ---------------------------------------------------
// start server
// ---------------------------------------------------
void serverStart()
{
  listenSocket = TcpOpen(0, listenPort);
  if (listenSocket != ~0)
  {
   if (TcpListen( listenSocket ) == 0)
   {
      // success…
    }
    else
    {
      writeLineEx(1, 3, "   [ TcpListen: Error listening on socket. ]");
      TcpClose(listenSocket);
      listenSocket = ~0;
    }
  }
  else
  {
    writeLineEx( 1, 3, "   [ TcpOpen: Error opening TCP Socket on port %d. (Error %d) ]", listenPort, IpGetLastError() );
  }
}
```

## Availability

| Since Version |
|---|
