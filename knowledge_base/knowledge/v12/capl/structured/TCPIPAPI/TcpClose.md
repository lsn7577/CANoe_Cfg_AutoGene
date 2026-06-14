# TcpClose

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long TcpClose( dword socket);
```

## Description

The function closes the TCP socket. Upon successful completion the passed socket is no longer valid.

In contrast to TcpShutdown the connection in each direction is closed and the resources for the socket in the stack are released.

As soon as the socket has been successfully closed, an OnTcpClose event is initiated once on the remote station.

## Return Values

0: The function completed successfully.

## Example

```c
void disconnectSocket( dword socket )
{
  if (socket != -1)
  {
    TcpClose(socket);
  }
}
```

## Availability

| Since Version |
|---|
