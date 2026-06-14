# TcpAbort

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long TcpAbort( dword socket);
```

## Description

The function closes the TCP socket immediately and sends a reset flag (RST) to the remote socket. The aborted socket is no longer valid.

In contrast to TcpClose and TcpShutdown, the connection is not closed by the regular FIN-ACK handshake.

The OnTcpClose callback will be called on the remote socket.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 12.0 SP3: method | 12.0 12.0 SP3: method | 13.0 | 13.0 | — | 4.0 4.0 SP3: method |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
