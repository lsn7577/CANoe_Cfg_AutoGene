# TcpReceive

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long TcpReceive( dword socket, char buffer[], dword size);
socket.Receive( char buffer[], dword size);
```

## Description

The function receives data into the specified buffer.

If the receive operation does not complete immediately the operation is performed asynchronously and the function will return SOCKET_ERROR (-1).

Use IpGetLastSocketError to get a more specific error code.

If the specific error code is WSA_IO_PENDING (997), this confirms an asynchronous receiving and is no receive error.

The CAPL callback OnTcpReceive will be called on completion (successful or not), provided it is implemented in the same CAPL program.

## Return Values

0: The function completed successfully.

## Example

You can find a further example in the Ethernet sample configuration Chat: Open configuration (only with installed Ethernet option available).

```c
void startReceive ( dword socket, char buffer[] )
{
  long result;
  result = TcpReceive( socket, buffer, elcount(buffer) );
  if (result == -1)
  {
    result = IpGetLastSocketError(socket);
    if (result != 997)
    {
      // failure
      writeLineEx( 1, 3, “TcpReceive error %d”, result);
    }
  }
  else
  {
    // failure
    writeLIneEx( 1, 3, “TcpReceive error %d”, result);
  }
}
```

## Availability

| Since Version |
|---|
