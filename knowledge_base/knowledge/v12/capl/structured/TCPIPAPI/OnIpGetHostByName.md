# OnIpGetHostByName

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnIpGetHostByName(long result, char hostname[], dword ipv4Address[], dword count);
```

## Description

The callback is called if a previous call of IpGetHostByName is returned with error code WSAEWOULDBLOCK (10035) and the dissolve of the address is completed.

## Return Values

—

## Availability

| Since Version |
|---|
