# OnSomeIpClosedIPv6TCPConnection

> Category: `IP` | Type: `function`

## Syntax

```c
void OnSomeIpClosedIPv6TCPConnection(byte localIPv6Address[], dword localPort, byte remoteIPv6Address[], dword remotePort);
```

## Description

This callback will be called after a IL’s TCP connection has been closed.

## Return Values

0: The function was successfully executed

## Example

```c
void OnSomeIpClosedIPv6TCPConnection(byte localIPv6Address[], dword localPort, byte remoteIPv6Address[], dword remotePort)
{
  char localAddrStr[128], remoteAddrStr[128];

  ipGetAddressAsString(localIPv6Address, localAddrStr, elcoun (localAddrStr));
  ipGetAddressAsString(remoteIPv6Address, remoteAddrStr, elcount(remoteAddrStr));

  write("Closed connection: [%s]:%d  <-> [%s]:%d", localAddrStr, localPort, remoteAddrStr, remotePort);
}
```

## Availability

| Since Version |
|---|
