# TcpOpen

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword TcpOpen( dword ipv4Address, dword port); // form 1
```

## Description

Depending on the address type, the function creates either an IPv4 or IPv6 TCP socket for use in connection-based, message-oriented communications. All parameters may be zero. If the port parameter is non-zero, the socket is implicitly bound to the given port. Otherwise the socket can be bound later on with IpBind or it will be automatically bound to a free port with TcpConnect.

Note:

If an address is given but the port is zero no implicit bind is performed. Please use IpBind after opening the socket in this case.

## Return Values

INVALID_SOCKET (~0): The function failed. Call IpGetLastError to get a more specific error code.

## Example

You can find a further example in the Ethernet sample configuration Chat: Open configuration (only with installed Ethernet option available).

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
      writeLineEx(1, 3, " [ TcpListen: Error listening on socket. ]");
      TcpClose(listenSocket);
      listenSocket = ~0;
    }
  }
  else
  {
    writeLineEx( 1, 3, " [ TcpOpen: Error opening TCP Socket on port %d. (Error %d) ]", listenPort, IpGetLastError() );
  }
}
```

## Availability

| Since Version |
|---|
