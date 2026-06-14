# IpGetSocketAddressFamily

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetSocketAddressFamily( dword socket);
```

## Description

The function returns the address family of the given socket.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |

## Example

```c
on start
{
  const dword INVALID_SOCKET = ~0; // invalid socket constant
  dword socket = INVALID_SOCKET;   // a socket
  char errMsg[255];                // error message buffer.
  byte ipv6Addr[16];
  dword port = 12345;
  long result;                     // function result

  // just create an socket.
  socket = UdpOpen(0 , port );
  result = IpGetSocketAddressFamily(socket);
  if (result != -1)
  {
    writeLineEx(1, 3, "IpGetSocketAddressFamily returned %d.", result);
  }
  else
  {
    writeLineEx(1, 3, "IpGetSocketAddressFamily: Invalid socket handle.");
  }

  // close the socket.
  UdpClose(socket);

  // ... and for IPv6 ...
  IpGetAddressAsArray(“::”, ipv6Addr); // get an IPv6 “zero” address
  socket = UdpOpen(ipv6Addr, 0);
  result = IpGetSocketAddressFamily(socket);
  if (result != -1)
  {
    writeLineEx(1, 3, "IpGetSocketAddressFamily returned %d.", result);
  }
  else
  {
    writeLineEx(1, 3, "IpGetSocketAddressFamily: Invalid socket handle.");
  }
  // close the socket.
  UdpClose(socket);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.2 SP2 | 13.0 | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
