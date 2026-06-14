# OnTcpReceive

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnTcpReceive( dword socket, long result, dword address, dword port, char buffer[], dword size); // form 1
```

## Description

If the CAPL program implements this callback it is called when a receive operation on a TCP socket completes.

The stack contains a data queue that is reduced by TcpReceive as soon as data are located there.

So that additional data from the data queue will be received in the future for the socket, TcpReceive must be called up again within the callback.

If result = 0 and size = 0, socket was closed by the communication peer, see example.

## Return Values

—

## Example

```c
variables
{
  const dword INVALID_SOCKET =  0;
  const dword SOCKET_ERROR   = -1;
  const long  WSA_IO_PENDING =  997;

  dword gSocket;  // socket handle
}

void foo()
{
  int rc = 0;
  char buffer[65*1024];

  rc = TcpReceive(gSocket, buffer, elcount(buffer));
  if (rc==0)
  {
    // The receive operation does complete immediately, so the callback
    // function OnTcpReceive was already called.
  }
  else if (rc==SOCKET_ERROR)
  {
    long ipLastErr;
    ipLastErr = IpGetLastSocketError(gSocket);
    if (ipLastErr==WSA_IO_PENDING)
    {
      // The receive operation is performed asynchronously
    }
    else
    {
      Write("TcpReceive: operation failed (IpGetLastSocketError=%d)", ipLastErr);
      TCPClose(gSocket);
      gSocket = INVALID_SOCKET;
    }
  }
  else
  {
    Write("TcpReceive: operation failed (%d)", rc);
    TCPClose(gSocket);
    gSocket = INVALID_SOCKET;
  }
}

void OnTcpReceive( dword socket, long result, dword address, dword port, char buffer[], dword size)
{
  if (result==0)
  {
    if (size==0)
    {
      // Size of zero indicates that the socket was closed by the communication peer.
      Write("OnTcpReceive: socket closed by peer");
      TCPClose(gSocket);
      gSocket = INVALID_SOCKET;
    }
    else
    {
      // Sucessfully received some bytes over the TCP/IP connection.
      // Do something useful with the data ...
      // ... and continue receiving ...
      foo ();
    }
  }
  else
  {
    long ipLastErr;
    ipLastErr = IpGetLastSocketError(gSocket);
    Write("OnTcpReceive: operation failed (result=%d IpGetLastSocketError=%d)", result, ipLastErr);
    TCPClose(gSocket);
    gSocket = INVALID_SOCKET;
  }
}
```

## Availability

| Since Version |
|---|
