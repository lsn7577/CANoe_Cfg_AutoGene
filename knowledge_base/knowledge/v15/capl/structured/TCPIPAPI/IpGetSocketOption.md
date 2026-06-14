# IpGetSocketOption

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetSocketOption( dword socket, char level[], char name[], long &value);
```

## Description

The function reads the value of the given socket option.

The function is dependent on the selected stack.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| level | The level at which the option is defined, e.g. SOL_SOCKET (0xFFFF). See Socket Options for all supported socket levels. |
| name | The socket option name to be read, e.g. SO_BROADCAST (0x0020). See Socket Options for all supported socket options. |
| value | The value of the socket option will be returned in this variable. |

## Example

```c
on start
{
  char errorMessage[255];
  long socket;
  long result;
  long value;

  // open a udp socket
  socket = udpOpen(0,0);
  if( socket == ~0 )
  {
    write("open udp socket failed. Last error was %d", ipGetLastError());
  }
  
  // get the socket type (UDP = 2, TCP = 1)
  result = ipGetSocketOption(socket, "SOL_SOCKET", "SO_TYPE", value);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(socket, errorMessage, elcount(errorMessage));
    write("Failed to get socket option SO_TYPE. Error: %s", errorMessage);
  }
  else
  {
    write("The socket type is %d", value);
  }
  result = ipGetSocketOption(socket, "IPPROTO_IP", "IP_TTL", value);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(socket, errorMessage, elcount(errorMessage));
    write("Failed to get socket option IP_TTL. Error: %s", errorMessage);
  }
  else
  {
    write("The IP TTL of this socket is %d", value);
  }
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
