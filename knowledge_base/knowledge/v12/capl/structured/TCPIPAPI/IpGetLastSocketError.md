# IpGetLastSocketError

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetLastSocketError( dword socket);
socket.GetLastSocketError();
```

## Description

The function returns the Winsock 2 error code of the last operation that failed on the specified socket.

## Return Values

WSA_INVALID_PARAMETER (87): The specified socket was invalid.

## Example

```c
on start
{
  const dword INVALID_SOCKET = ~0; // invalid socket constant
  dword socket = INVALID_SOCKET;   // a socket

  // just create an unspecified socket.
  socket = UdpOpen( 0, 0 );

  // produce an error e.g. using invalid parameters to UdpSendTo
  if (UdpSendTo(socket, 0, 0, "a", 1) == -1)
  {
    writeLineEx(1, 3, "IpGetLastSocketError: %d", IpGetLastSocketError(socket));
  }

  // close the socket.
  UdpClose(socket);
}
```

## Availability

| Since Version |
|---|
