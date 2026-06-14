# OnTcpConnect

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnTcpConnect( dword socket, long result);
```

## Description

If the CAPL program implements this callback it is called when an asynchronous connection operation completes. This means that the connection to the remote station has been established. It is not yet certain at this time that the remote station has accepted the connection with TcpAccept.

If a listen socket of a remote station is blocked, error 10061 (Connection refused) is output in the result parameter.

## Return Values

—

## Example

```c
// ---------------------------------------------------
// connect a client and return the socket handle
// ---------------------------------------------------
dword clientConnect(dword targetIP, dword port)
{
  dword resultSocket = TcpOpen ( 0, 0 );
  if (resultSocket != ~0)
  {
    TcpConnect ( resultSocket, targetIP, port );
    // => Connection established in callback OnTcpConnect...
  }
  else
  {
    writeLineEx(1, 3, " [ TcpOpen: FAILED. ]");
  }
  return resultSocket;
}

// ---------------------------------------------------
// Connection operation completes
// ---------------------------------------------------
void OnTcpConnect( dword socket, long result)
{
  if (result == 0)
  {
    // start receiving on socket using TcpReceive …
  }
  else
  {
    writeLineEx(1, 3, “OnTcpConnect error %d”, result”);
  }
}
```

## Availability

| Since Version |
|---|
