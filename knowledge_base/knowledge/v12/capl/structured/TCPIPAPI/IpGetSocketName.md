# IpGetSocketName

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetSocketName( dword socket, dword &ipv4Address, dword &port); // form 1
socket.GetSocketName(dword &ipv4Address, dword &port); // form 1
```

## Description

The function returns the local bound address and port of a socket.

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  LONG  ipv4SocketHandle;
  DWORD port;
  DWORD ipv4Address[1];
  CHAR  data[255];
  CHAR  addressStr[49];

  // open a IPv4 UDP socket. This will lead to an implicit bind
  ipGetAdapterAddress(1,ipv4Address, elcount(ipv4Address));
  ipv4SocketHandle = udpOpen(ipv4Address[0], 123);
  if(ipv4SocketHandle == ~0)
  {
    writeLineEx(1, 3, "%BASE_FILE_NAME%: failed to open the socket. Error code: %d", ipGetLastError());
  }

  // get the local bound address and port
  ipGetSocketName(ipv4SocketHandle, ipv4Address[0], port);
  ipGetAddressAsString(ipv4Address[0], addressStr, elcount(addressStr));
  writeLineEx(1, 1, "%BASE_FILE_NAME%: The IPv4 socket is bound to address %s and port %d", addressStr, port);
}
```

## Availability

| Since Version |
|---|
