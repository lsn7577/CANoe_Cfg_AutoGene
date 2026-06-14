# TcpSend

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long TcpSend( dword socket, char buffer[], dword size); // from 1
long TcpSend( dword socket, struct data[], dword size); // from 2
long TcpSend( dword socket, byte buffer[], dword size); // from 3
```

## Description

The function sends data on the specified socket. If the send operation does not complete immediately the operation is performed asynchronously and the function will return SOCKET_ERROR (-1).

Use IpGetLastSocketError to get a more specific error code. If the specific error code is WSA_IO_PENDING (997), this indicates an asynchronous sending.

The CAPL callback OnTcpSend will be called on completion (successful or not), providing that it is implemented in the same CAPL program.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| buffer | The buffer containing the data to be sent. |
| data | The struct containing the data to be sent. |
| size | The size of the data to be sent. |

## Example

```c
// ---------------------------------------------------
// send tcp data.
// ---------------------------------------------------
void sendTcpData( dword socket, char data[] )
{
  long result;
  dword size;

  size = elcount(data);
  result = TcpSend(socket, data, size);
  if (result == 0)
  {
    // sending took place immediately.
    // => OnTcpSend is NOT called.
  }
  else
  {
    if (result == -1)
    {
      result = IpGetLastSocketError(socket);
      if (result == 997)
      {
        // sending is done asynchronously.
        // => OnTcpSend is called when done sending.
      }
      else
      {
        writeLineEx( 1, 3, "   [ sendTcpData: Error sending data. (%d) ]", result);
      }
    }
    else
    {
      writeLineEx( 1, 3, "   [ sendTcpData: Error sending data. (%d) ]", result);
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 7.0: function 1 7.0 SP5: method 1 8.2 SP2: function/method 2-3 | 13.0 | 13.0: form 3 | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
