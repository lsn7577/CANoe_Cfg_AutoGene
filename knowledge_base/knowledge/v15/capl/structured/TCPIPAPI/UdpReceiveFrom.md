# UdpReceiveFrom

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long UdpReceiveFrom( dword socket, char buffer[], dword size);
```

## Description

The function receives data into the specified buffer. If the receive operation does not complete immediately the operation is performed asynchronously and the function will return SOCKET_ERROR (-1). Use IpGetLastSocketError to get a more specific error code. If the specific error code is WSA_IO_PENDING (997) the CAPL callback OnUdpReceiveFrom will be called on completion (successful or not), provided it is implemented in the same CAPL program.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| buffer | The buffer used to store the incoming data. |
| size | The size of the data buffer. |

## Example

See example Create UDP Server Sockets.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 7.0 7.0 SP5: method | 13.0 | 13.0 | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
