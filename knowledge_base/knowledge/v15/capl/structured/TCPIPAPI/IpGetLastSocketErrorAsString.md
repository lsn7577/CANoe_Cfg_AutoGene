# IpGetLastSocketErrorAsString

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetLastSocketErrorAsString( dword socket, char text[], dword count);
```

## Description

The function retrieves the error message of the last operation that failed on the specified socket (see Winsock 2 error code).

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| text | The buffer used to store the error message. |
| count | The size of the text buffer. |

## Example

```c
on start
{
  const dword INVALID_SOCKET = ~0; // invalid socket constant
  dword socket = INVALID_SOCKET;   // a socket
  char errMsg[255];                // error message buffer.

  // just create an unspecified socket.
  socket = UdpOpen( 0, 1 );

  // produce an error e.g. using invalid parameters to UdpSendTo
  if (UdpSendTo(socket, 0, 0, "a", 1) == -1)
  {
    IpGetLastSocketErrorAsString( socket, errMsg, elcount(errMsg) );
    writeLineEx(1, 3, "IpGetLastSocketErrorAsString: %s", errMsg);
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
