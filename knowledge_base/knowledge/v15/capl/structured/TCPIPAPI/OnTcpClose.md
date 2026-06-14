# OnTcpClose

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnTcpClose( dword socket, long result);
```

## Description

If the CAPL program implements this callback it is called when a TCP socket receives a close notification, when the remote station terminates the connection with TcpClose or TcpShutdown.

To release the resources of the socket, TcpClose must be called.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle or socket object. |
| result | The specific result code of the operation. If the operation completed successfully the value is 0. Otherwise the value is an error code.Typical errors are interrupt of the connection, timeout or reset. |

## Return Values

—

## Example

```c
// ---------------------------------------------------
// TCP socket receives a close notification
// ( remote disconnected )
// ---------------------------------------------------

void OnTcpClose( dword socket, long result)
{
  writeLineEx(1, 1, " [ OnTcpClose called. (socket: %d, result: %d) ]", socket, result);
  TcpClose(socket);
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
