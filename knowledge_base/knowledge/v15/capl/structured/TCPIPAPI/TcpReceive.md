# TcpReceive

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long TcpReceive( dword socket, char buffer[], dword size); // form 1
long TcpReceive( dword socket ); // form 2
long TcpReceive( dword socket, dword bytesToReceive ); // form 3
long TcpReceive( dword socket, dword bytesToReceive, char buffer[] ); // form 4
long TcpReceive( dword socket, dword bytesToReceive, dword offset, char buffer[] ); // form 5
long TcpReceive( dword socket, dword bytesToReceive, byte buffer[] ); // form 6
long TcpReceive( dword socket, dword bytesToReceive, dword offset, byte buffer[] ); // form 7
```

## Description

The function receives data on the given socket.

The received data will be returned in the CAPL callback OnTcpReceive in every case.

If the receive operation does not complete immediately the operation is performed asynchronously and the function will return SOCKET_ERROR (-1).

Use IpGetLastSocketError to get a more specific error code.

If the specific error code is WSA_IO_PENDING (997), this confirms an asynchronous receiving and is no receive error.

The CAPL callback OnTcpReceive will be called on completion (successful or not), provided it is implemented in the same CAPL program.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| buffer | The buffer used to store the incoming data. |
| size | The size of the data buffer. |
| bytesToReceive | The amount of data that has to be received before the OnTcpReceive callback will be called. This is limited by the internal receive buffer size. |
| offset | The offset where the received data will be written in the given buffer. |

## Example

You can find further examples in the Ethernet chat sample configurations Open Folder (only with installed Ethernet option available).

```c
void startReceive ( dword socket, char buffer[] )
{
  long result;
  result = TcpReceive( socket, buffer, elcount(buffer) );
  if (result == -1)
  {
    result = IpGetLastSocketError(socket);
    if (result != 997)
    {
      // failure
      writeLineEx( 1, 3, “TcpReceive error %d”, result);
    }
  }
  else
  {
    // failure
    writeLIneEx( 1, 3, “TcpReceive error %d”, result);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: form 1 15: form 2-7 | 7.0: syntax 1 7.0 SP5: method 1 15: form 2-7 | 13.0: form 1 15: form 2-7 | 13.0: form 1 15: form 2-7 | — | 2.0 SP2: form 1 15: form 2-7 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
