# TcpSend

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long TcpSend( dword socket, char buffer[], dword size);
socket.Send( char buffer[], dword size);
```

## Description

The function sends data on the specified socket. If the send operation does not complete immediately the operation is performed asynchronously and the function will return SOCKET_ERROR (-1).

Use IpGetLastSocketError to get a more specific error code. If the specific error code is WSA_IO_PENDING (997), this indicates an asynchronous sending.

The CAPL callback OnTcpSend will be called on completion (successful or not), providing that it is implemented in the same CAPL program.

If the function returns with 0, the data were able to be sent immediately (synchronously). In this case OnTcpSend is NOT called up.For this reason you must relocate the code in OnTcpSend to a function or call up OnTcpSend explicitly.

## Return Values

0: The function completed successfully.

## Example

```c
// ---------------------------------------------------
// send tcp data.
// ---------------------------------------------------
void sendTcpData( dword socket, char data[] )
{
  long result;
  dword size;

  size = elcount(data);
  result = TcpSend(socket, data, size);
  if (result == 0)
  {
    // sending took place immediately.
    // => OnTcpSend is NOT called.
  }
  else
  {
    if (result == -1)
    {
      result = IpGetLastSocketError(socket);
      if (result == 997)
      {
        // sending is done asynchronously.
        // => OnTcpSend is called when done sending.
      }
      else
      {
        writeLineEx( 1, 3, "   [ sendTcpData: Error sending data. (%d) ]", result);
      }
    }
    else
    {
      writeLineEx( 1, 3, "   [ sendTcpData: Error sending data. (%d) ]", result);
    }
  }
}
```

## Availability

| Since Version |
|---|
