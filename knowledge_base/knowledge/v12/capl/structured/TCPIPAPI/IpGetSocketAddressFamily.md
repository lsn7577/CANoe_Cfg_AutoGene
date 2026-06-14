# IpGetSocketAddressFamily

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetSocketAddressFamily( dword socket);
```

## Description

The function returns the address family of the given socket.

## Return Values

AF_INET (2): The socket belongs to the IPv4 address family.

## Example

```c
on start
{
  const dword INVALID_SOCKET = ~0; // invalid socket constant
  dword socket = INVALID_SOCKET;   // a socket
  char errMsg[255];                // error message buffer.
  byte ipv6Addr[16];
  dword port = 12345;
  long result;                     // function result

  // just create an socket.
  socket = UdpOpen(0 , port );
  result = IpGetSocketAddressFamily(socket);
  if (result != -1)
  {
    writeLineEx(1, 3, "IpGetSocketAddressFamily returned %d.", result);
  }
  else
  {
    writeLineEx(1, 3, "IpGetSocketAddressFamily: Invalid socket handle.");
  }

  // close the socket.
  UdpClose(socket);

  // ... and for IPv6 ...
  IpGetAddressAsArray(“::”, ipv6Addr); // get an IPv6 “zero” address
  socket = UdpOpen(ipv6Addr, 0);
  result = IpGetSocketAddressFamily(socket);
  if (result != -1)
  {
    writeLineEx(1, 3, "IpGetSocketAddressFamily returned %d.", result);
  }
  else
  {
    writeLineEx(1, 3, "IpGetSocketAddressFamily: Invalid socket handle.");
  }
  // close the socket.
  UdpClose(socket);
}
```

## Availability

| Since Version |
|---|
