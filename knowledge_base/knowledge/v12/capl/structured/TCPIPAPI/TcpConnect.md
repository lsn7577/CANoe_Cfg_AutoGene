# TcpConnect

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long TcpConnect( dword socket, dword address, dword port); // form 1
socket.Connect( dword address, dword port); // form 1
```

## Description

The function establishes a connection with the specified location.

Use IpGetLastSocketError to get a more specific error code. The specific error code is WSAWOULDBLOCK (10035), is no “real” error, but just confirms the non-blocking socket behavior. A real connection error is different from error 10035.

The CAPL callback OnTcpConnect will be called on completion (successful or not), provided it is implemented in the same CAPL program.

On the remote station OnTcpListen is called up, which accepts the connection with TcpAccept.

## Return Values

WSA_INVALID_PARAMETER (87): The specified socket was invalid.

## Example

```c
// ---------------------------------------------------
// connect a client...
// ---------------------------------------------------
void clientConnect()
{
  dword result;
  clientSocket = TcpOpen( 0, 0 );
  if (clientSocket != INVALID_SOCKET)
  {
    result = TcpConnect( clientSocket, ipv4Addr[0], listenPort );
    if ( result == -1)
    {
      result = IpGetLastSocketError(clientSocket);
      if ( result != 10035)
      {
        writeLineEx( 1, 3, " [ TcpConnect for client failed with error %d ]", result );
      }
    }
    else
    {
      writeLineEx(1, 3, " [ TcpConnect error %d ]", result);
    };
  }
  else
  {
    writeLineEx(1, 3, " [ TcpOpen: FAILED. ]");
  }
}
```

## Availability

| Since Version |
|---|
