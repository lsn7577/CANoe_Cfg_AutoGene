# OnTcpClose

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnTcpClose( dword socket, long result);
```

## Description

If the CAPL program implements this callback it is called when a TCP socket receives a close notification, when the remote station terminates the connection with TcpClose or TcpShutdown.

To release the resources of the socket, TcpClose must be called.

## Return Values

—

## Example

```c
// ---------------------------------------------------
// TCP socket receives a close notification
// ( remote disconnected )
// ---------------------------------------------------

void OnTcpClose( dword socket, long result)
{
  writeLineEx(1, 1, " [ OnTcpClose called. (socket: %d, result: %d) ]", socket, result);
  TcpClose(socket);
}
```

## Availability

| Since Version |
|---|
