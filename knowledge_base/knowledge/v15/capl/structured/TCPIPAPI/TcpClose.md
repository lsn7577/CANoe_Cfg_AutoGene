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

## Parameters

| Name | Description |
|---|---|
| socket | The socket to be closed. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 7.0 7.0 SP5: method | 13.0 | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
