# OnTcpListen

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnTcpListen( dword socket, long result)
```

## Description

If the CAPL program implements this callback it is called when TcpListen was called and a connection request for the specified socket is received.

The connection must be accepted with TcpAccept because the listen socket otherwise remains blocked for other clients. This block is evident for a client in OnTcpConnect from the output of error code 10061 (Connection refused).

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle or socket object. If the handle is valid (not equal to ~0), it corresponds to the socket that was used for TcpListen. |
| result | The specific result code of the operation. If the operation completed successfully the value is zero. Otherwise the value is an error code. |

## Return Values

—

## Example

```c
// ---------------------------------------------------
// Callback when client connects to server's listen socket.
// ---------------------------------------------------
void OnTcpListen( dword socket, long result)
{
  dword newSocket;
  newSocket = TcpAccept( socket );
  if (newSocket != ~0)
  {
    // start to receive data on the new socket...
  }
  else
  {
    writeLineEx( 1, 3, "S: TcpAccept: Socket error: %d", IpGetLastSocketError (socket) );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 7.0 | 13.0 | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
