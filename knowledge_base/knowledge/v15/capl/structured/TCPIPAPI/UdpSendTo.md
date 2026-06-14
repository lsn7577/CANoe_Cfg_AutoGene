# UdpSendTo

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long UdpSendTo( dword socket, dword address, dword port, char buffer[], dword size); // form 1
long UdpSendTo( dword socket, byte ipv6Address[], dword port, char buffer[], dword size); // form 2
long UdpSendTo( dword socket, dword address, dword port, struct data[], dword size); // form 3
long UdpSendTo( dword socket, dword address, dword port, byte buffer[], dword size); // form 4
long UdpSendTo( dword socket, byte ipv6Address[], dword port, struct data[], dword size); // form 5
long UdpSendTo( dword socket, byte ipv6Address[], dword port, byte buffer[], dword size); // form 6
long UdpSendTo( dword socket, IP_Endpoint remoteEndpoint, char buffer[], dword size); // form 7
long UdpSendTo( dword socket, IP_Endpoint remoteEndpoint, byte buffer[], dword size); // form 8
long UdpSendTo( dword socket, IP_Endpoint remoteEndpoint, struct data[], dword size); // form 9
```

## Description

The function sends data to the specified location. If the send operation does not complete immediately the operation is performed asynchronously and the function will return SOCKET_ERROR (-1). Use IpGetLastSocketError to get a more specific error code. If the specific error code is WSA_IO_PENDING (997) and the CAPL callback OnUdpSendTo will be called on completion (successful or not), providing that it is implemented in the same CAPL program.

If the operation has been processed synchronously, the CAPL callback OnUdpSendTo is not called up (see also TcpSend).

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| address | The numerical IPv4 address of the destination in network-byte order. |
| ipv6Address | The destination IPv6 address in a 16 byte array. |
| port | The port of the destination in host-byte order. |
| buffer | The buffer containing the data to be sent. |
| data | The struct containing the data to be sent. |
| size | The size of the data to be sent. |
| remoteEndpoint | The destination endpoint. IP address and port number must be specified. Example: IP_Endpoint( 192.168.1.1:40001 ) IP_Endpoint( [FC00::0001]:40001 ) |

## Example

```c
variables
{
  UdpSocket gSocket;
  char gRxBuffer[1000];
}

on start
{
  gSocket = UdpSocket::Open( IP_Endpoint(0.0.0.0:40001) );
  gSocket.SendTo( IP_Endpoint(192.168.0.2:40002), "Hello", 5 );
  gSocket.ReceiveFrom( gRxBuffer, elcount( gRxBuffer) );
}

OnUdpReceiveFrom( UdpSocket socket, long result, IP_Endpoint remoteEndpoint, char buffer[], dword size)
{
  if (result == 0)
  {
    write( "Received: %s", buffer );
    gSocket.ReceiveFrom( gRxBuffer, elcount( gRxBuffer) );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: function 1-2 12.0: function/method 7-9 | 7.0: function 1-2 7.0 SP5: method 1-2 8.2 SP2: function/method 3-6 12.0: function/method 7-9 | 13.0 | 13.0: form 7-9 | — | 2.0 SP2: function 1-2 12.0: function/method 7-9 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
