# tlsAuthenticateAsServer

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
long tlsAuthenticateAsServer(dword socket, char certificate[]);
```

## Description

Starts the authentication handshake as server.

## Return Values

0: The function completed successfully.

## Example

```c
void OnTcpListen( dword socket, long result)
{
  DWORD clientHandle;
  // Accept the connection
  clientHandle = TcpAccept( socket );

  tlsOpen(clientHandle);
  tlsAuthenticateAsServer(clientHandle, "Server1");

  if ((tlsGetLastError(clientHandle) != 0) &&
  (tlsGetLastError(clientHandle) != 997))
  {
    // an error occurred
    return;
  }
}
```

## Availability

| Since Version |
|---|
