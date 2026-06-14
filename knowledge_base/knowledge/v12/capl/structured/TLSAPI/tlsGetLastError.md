# tlsGetLastError

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
long tlsGetLastError(dword socket);
```

## Description

Returns the TLS error code of the last operation that failed on a specified socket.

## Return Values

WSA_INVALID_PARAMETER (87): The specified socket was invalid.

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
