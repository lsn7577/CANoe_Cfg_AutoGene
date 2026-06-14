# tlsAuthenticateAsClient

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
long tlsAuthenticateAsClient(dword socket, char serverName[]);
```

## Description

Starts the authentication handshake as client.

## Return Values

0: The function completed successfully.

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
