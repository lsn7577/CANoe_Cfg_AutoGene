# IpGetLastSocketErrorAsString

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetLastSocketErrorAsString( dword socket, char text[], dword count);
socket.GetLastSocketErrorAsString( char text[], dword count);
```

## Description

The function retrieves the error message of the last operation that failed on the specified socket (see Winsock 2 error code).

## Return Values

0: The error message was written into the text buffer. In case of an invalid error code, the error message has the format "Unknown error: x" assuming the last error code x for the specified socket.

## Example

```c
on start
{
  const dword INVALID_SOCKET = ~0; // invalid socket constant
  dword socket = INVALID_SOCKET;   // a socket
  char errMsg[255];                // error message buffer.

  // just create an unspecified socket.
  socket = UdpOpen( 0, 1 );

  // produce an error e.g. using invalid parameters to UdpSendTo
  if (UdpSendTo(socket, 0, 0, "a", 1) == -1)
  {
    IpGetLastSocketErrorAsString( socket, errMsg, elcount(errMsg) );
    writeLineEx(1, 3, "IpGetLastSocketErrorAsString: %s", errMsg);
  }

  // close the socket.
  UdpClose(socket);
}
```

## Availability

| Since Version |
|---|
