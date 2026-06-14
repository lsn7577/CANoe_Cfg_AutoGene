# OnUdpReceiveFrom

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnUdpReceiveFrom( dword socket, long result, dword address, dword port, char buffer[], dword size); // form 1
void OnUdpReceiveFrom( dword socket, long result, dword address, dword port, byte buffer[], dword size); // form 2
void OnUdpReceiveFrom( dword socket, long result, byte ipv6Address[], dword port, char buffer[], dword size); // form 3
void OnUdpReceiveFrom( dword socket, long result, byte ipv6Address[], dword port, byte buffer[], dword size); // form 4
void OnUdpReceiveFrom( dword socket, long result, IP_Endpoint remoteEndpoint, char buffer[], dword size); // form 5
void OnUdpReceiveFrom( dword socket, long result, IP_Endpoint remoteEndpoint, byte buffer[], dword size); // form 6
```

## Description

If the CAPL program implements this callback it is called when an asynchronous receive operation on an UDP socket completes.

The stack contains a data queue that is reduced by UdpReceiveFrom as soon as data are located there.

So that additional data from the data queue will be received in the future for the socket, UdpReceiveFrom must be called up again within the callback.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle or socket object. |
| result | The result code of the asynchronous operation. If the operation completed successfully the value is 0. Otherwise the value is an error code. |
| address | The numerical remote IPv4 address of the location which sent the data. |
| ipv6Address | The remote IPv6 address in a 16 byte array. |
| port | The remote port of the location which sent the data in host-byte order. |
| buffer | The buffer into which the data was stored. |
| size | The number of bytes received. |
| remoteEndpoint | The remote endpoint of the location which sent the data. |

## Return Values

—

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
| Since Version | 8.5: form 1, 3 10.0 SP3: form 2, 4 12.0: form 5-6 | 7.0: form 1, 3 10.0 SP3: form 2, 4 12.0: form 5-6 | 13.0 | — | — | 2.0 SP2: form 1, 3 2.2 SP2: form 2, 4 4.0: form 5-6 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
