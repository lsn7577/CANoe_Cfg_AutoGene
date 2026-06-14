# IpSetSocketOption

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpSetSocketOption( dword socket, long level, long name, long value); // form 1
long IpSetSocketOption( dword socket, char level[], char name[], long value); // form 2
```

## Description

The function modifies a socket option.

The function is dependent on the selected stack.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| level | The level at which the option is defined, e.g. SOL_SOCKET (0xFFFF). See Socket Options for all supported socket levels. |
| name | The socket option name to be modified, e.g. SO_BROADCAST (0x0020). See Socket Options for all supported socket options. |
| value | The value to be set for the socket option. |

## Example

```c
on start
{
  CHAR errorMessage[255];
  LONG tcpSocket;
  LONG result;
  LONG value;

  // open a tcp socket
  tcpSocket = tcpOpen(0,0);
  if( tcpSocket == ~0 )
  {
    write("open tcp socket failed. Last error was %d", ipGetLastError());
  }

  // activate SO_KEEPALIVE on the tcp socket
  result = ipSetSocketOption(tcpSocket, "SOL_SOCKET", "SO_KEEPALIVE", 1);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(tcpSocket, errorMessage, elcount(errorMessage));
    write("Failed to set socket option SO_KEEPALIVE. Error: %s", errorMessage);
  }

  // set Time to live it is greater than 32
  result = ipGetSocketOption(tcpSocket, "IPPROTO_IP", "IP_TTL", value);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(tcpSocket, errorMessage, elcount(errorMessage));
    write("Failed to get socket option IP_TTL. Error: %s", errorMessage);
  }
  if( value > 32 )
  {
    result = ipSetSocketOption(tcpSocket, "IPPROTO_IP", "IP_TTL", 32);
    if( result != 0 )
    {
      ipGetLastSocketErrorAsString(tcpSocket, errorMessage, elcount(errorMessage));
      write("Failed to set socket option IP_TTL. Error: %s", errorMessage);
    }
  }

  // avoid tcp to use the nagle algorithm
  result = ipSetSocketOption(tcpSocket, "IPPROTO_TCP", "TCP_NODELAY", 1);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(tcpSocket, errorMessage, elcount(errorMessage));
    write("Failed to get socket option TCP_NODELAY. Error: %s", errorMessage);
  }

  // connect the socket
  result = tcpConnect(tcpSocket, IpGetAddressAsNumber("192.168.1.2"), 21);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(tcpSocket, errorMessage, elcount(errorMessage));
    write("Failed to get socket option TCP_NODELAY. Error: %s", errorMessage);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 7.0: function 1 7.0 SP5: method 1 8.2 SP2: function/method 2 | 13.0 | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
