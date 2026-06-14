# tlsOpen

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
dword tlsOpen(dword socket);
```

## Description

Opens a TLS socket. An existing socket handle is used to create a new TLS connection.

## Return Values

INVALID_SOCKET (~0): The function failed. Call tlsGetLastError to get a more specific error code.

## Example

```c
void OnTcpConnect( dword socket, long result)
{
  if (result == 0)
  {
    socket = tlsOpen(socket);
    tlsAuthenticateAsClient(socket, "");

    if ((tlsGetLastError(socket) != 0) &&
    (tlsGetLastError(socket) != 997))
    {
      // an error occurred
      return;
    }
  }
}
```

## Availability

| Since Version |
|---|
