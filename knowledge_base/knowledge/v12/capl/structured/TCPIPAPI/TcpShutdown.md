# TcpShutdown

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long TcpShutdown( dword socket);
socket.Shutdown( dword socket);
```

## Description

The function disables send operations on the specified socket. This function may be used to shutdown a TCP connection. Data can thereby still be received.

When this function is used the socket (in contrast to TcpClose) is closed only for the sending direction.

The remote station is informed about this with event procedure OnTcpClose.

The remote station cannot recognize whether TcpClose or TcpShutdown was used. For this reason the application or protocol must clearly control how a node behaves.

An example of a TcpShutdown can be a web service. The client sends a request to the server and then immediately closes its connection (in the sending direction). The server recognizes from this that the request is finished and sends the response to the client. The client receives the information on the socket closed in the sending direction and closes the connection with TcpClose.

In contrast to this an FTP protocol behaves by using a connection to control a permanent dialog between the nodes. The connection is completely closed by a special termination command.

## Return Values

0: The function completed successfully.

## Availability

| Since Version |
|---|
