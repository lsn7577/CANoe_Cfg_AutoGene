# OnAREthEstablishedIPv6TCPConnection

> Category: `IP` | Type: `function`

## Syntax

```c
void OnAREthEstablishedIPv6TCPConnection(byte localIPv6Address[], dword localPort, byte remoteIPv6Address[], dword remotePort)
```

## Description

This callback will be called after an incoming or outgoing TCP connection has been established for an IL’s application endpoint

## Return Values

0: The function was successfully executed

## Example

```c
void OnAREthEstablishedIPv6TCPConnection(byte localIPv6Address[], dword localPort, byte remoteIPv6Address[], dword remotePort)
{
  char localAddrStr[128], remoteAddrStr[128];

  ipGetAddressAsString(localIPv6Address, localAddrStr, elcount(localAddrStr));
  ipGetAddressAsString(remoteIPv6Address, remoteAddrStr, elcount(remoteAddrStr));

  write("Established connection: [%s]:%d  <-> [%s]:%d", localAddrStr, localPort, remoteAddrStr, remotePort);
}
```

## Availability

| Since Version |
|---|
