# OnTcpConnect

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnTcpConnect( dword socket, long result);
```

## Description

If the CAPL program implements this callback it is called when an asynchronous connection operation completes. This means that the connection to the remote station has been established. It is not yet certain at this time that the remote station has accepted the connection with TcpAccept.

If a listen socket of a remote station is blocked, error 10061 (Connection refused) is output in the result parameter.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle or socket object. |
| result | The specific result code of the operation. If the operation completed successfully the value is 0. Otherwise the value is an error code. Error code 10061 (Connection refused): The listen socket of a server is occupied by another connection that has not yet been accepted with TcpAccept. Because the internal queue for incoming connections is set to 1 in CANoe, only one node can ever queue up there. All other nodes are refused with error 10061. |

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
