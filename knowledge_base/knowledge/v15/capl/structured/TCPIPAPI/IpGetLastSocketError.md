# IpGetLastSocketError

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetLastSocketError( dword socket);
```

## Description

The function returns the Winsock 2 error code of the last operation that failed on the specified socket.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |

## Example

```c
on start
{
  const dword INVALID_SOCKET = ~0; // invalid socket constant
  dword socket = INVALID_SOCKET;   // a socket

  // just create an unspecified socket.
  socket = UdpOpen( 0, 0 );

  // produce an error e.g. using invalid parameters to UdpSendTo
  if (UdpSendTo(socket, 0, 0, "a", 1) == -1)
  {
    writeLineEx(1, 3, "IpGetLastSocketError: %d", IpGetLastSocketError(socket));
  }

  // close the socket.
  UdpClose(socket);
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
