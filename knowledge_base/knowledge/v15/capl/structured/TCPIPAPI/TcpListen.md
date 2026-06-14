# TcpListen

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long TcpListen( dword socket);
```

## Description

The function causes the socket to listen for incoming connection requests, which will be provided in the CAPL callback OnTcpListen, if it is implemented in the same CAPL program. If the operation fails, the function will return SOCKET_ERROR (-1). Use IpGetLastSocketError to get a more specific error code.

The socket must have been opened beforehand with TcpOpen and be bound at least to one port. The binding to the port is carried out during opening or using IpBind.

The additional binding to an IP address is optional.

Incoming connections on the listen socket must be accepted with TcpAccept because all other connections will otherwise be refused with error10061 (Connection refused).

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |

## Example

```c
// ---------------------------------------------------
// start server
// ---------------------------------------------------
void serverStart()
{
  listenSocket = TcpOpen(0, listenPort);
  if (listenSocket != ~0)
  {
   if (TcpListen( listenSocket ) == 0)
   {
      // success…
    }
    else
    {
      writeLineEx(1, 3, "   [ TcpListen: Error listening on socket. ]");
      TcpClose(listenSocket);
      listenSocket = ~0;
    }
  }
  else
  {
    writeLineEx( 1, 3, "   [ TcpOpen: Error opening TCP Socket on port %d. (Error %d) ]", listenPort, IpGetLastError() );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 7.0 7.0 SP5: method | 13.0 | 13.0 | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
