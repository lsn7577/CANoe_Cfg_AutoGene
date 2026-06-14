# UdpSend

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long UdpSend( dword socket, char buffer[], dword size); // form 1
long UdpSend( dword socket, struct data, dword size); // from 2
long UdpSend( dword socket, byte buffer[], dword size); // from 3
```

## Description

The function sends data on a connected UDP socket. It is necessary to connect the socket with UdpConnect in front of calling this function.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| buffer | The buffer containing the data to be sent. |
| data | The struct containing the data to be sent. |
| size | The size of the data to be sent. |

## Example

```c
variables
{
  UdpSocket gSocket;
}

on start
{
  gSocket = UdpSocket::Open( IP_Endpoint(0.0.0.0:0) );
  gSocket.Connect(ip_Endpoint(192.168.1.3:40002));
  gSocket.Send( "Request", 7 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
