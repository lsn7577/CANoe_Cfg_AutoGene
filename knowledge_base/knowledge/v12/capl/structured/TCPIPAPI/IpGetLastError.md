# IpGetLastError

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetLastError();
```

## Description

The function returns the Winsock 2 error code of the last operation that failed.

## Return Values

The error code as provided by the Winsock 2 WSAGetLastError function.

## Example

```c
on start
{
  // produces an error 10049...
  TcpOpen(0xffffffff, 1);

  writeLineEx(1, 3, "IpGetLastError: %d", IpGetLastError());
}
```

## Availability

| Since Version |
|---|
