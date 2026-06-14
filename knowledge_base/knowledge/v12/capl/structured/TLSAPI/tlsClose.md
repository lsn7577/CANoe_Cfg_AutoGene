# tlsClose

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
long tlsClose(dword socket, dword closeUnderlyingSocket);
```

## Description

Closes the given TLS connection. This sends a TLS alert message to the peer node. The underlaying socket will be closed automatically if the parameter closeUnderlyingSocket is set to a value greater 0.

## Return Values

0: The function completed successfully.

## Example

```c
void ClientStop()
{
  //
  // Close TLS socket and underlying socket
  //

  tlsClose(gTlsClientSocket, 1);
  gTlsClientSocket = 0;
}
```

## Availability

| Since Version |
|---|
