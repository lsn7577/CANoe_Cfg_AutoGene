# OnTcpReceive

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnTcpReceive( dword socket, long result, dword address, dword port, char buffer[], dword size); // form 1
void OnTcpReceive( dword socket, long result, dword address, dword port, byte buffer[], dword size); // form 2
void OnTcpReceive( dword socket, long result, byte ipv6Address[], dword port, char buffer[], dword size); // form 3
void OnTcpReceive( dword socket, long result, byte ipv6Address[], dword port, byte buffer[], dword size); // form 4
void OnTcpReceive( dword socket, long result, IP_Endpoint remoteEndpoint, char buffer[], dword size); // form 5
void OnTcpReceive( dword socket, long result, IP_Endpoint remoteEndpoint, byte buffer[], dword size); // form 6
```

## Description

If the CAPL program implements this callback it is called when a receive operation on a TCP socket completes.

The stack contains a data queue that is reduced by TcpReceive as soon as data are located there.

So that additional data from the data queue will be received in the future for the socket, TcpReceive must be called up again within the callback.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle or socket object. |
| result | The specific result code of the operation. If the operation completed successfully the value is zero. Otherwise the value is an error code. If result = 0 and size = 0, socket was closed by the communication peer, see example. |
| address | The numerical remote IPv4 address of the location which sent the data. |
| ipv6Address | The remote IPv6 address in a 16 byte array. |
| port | The remote port of the location which sent the data in host-byte order. |
| buffer | The buffer into which the data was stored. |
| size | The size of the received data. If result = 0 and size = 0, socket was closed by the communication peer, see example. |
| remoteEndpoint | The remote endpoint of the location which sent the data. |

## Return Values

—

## Example

```c
variables
{
  const dword INVALID_SOCKET =  0;
  const dword SOCKET_ERROR   = -1;
  const long  WSA_IO_PENDING =  997;

  dword gSocket;  // socket handle
}

void foo()
{
  int rc = 0;
  char buffer[65*1024];

  rc = TcpReceive(gSocket, buffer, elcount(buffer));
  if (rc==0)
  {
    // The receive operation does complete immediately, so the callback
    // function OnTcpReceive was already called.
  }
  else if (rc==SOCKET_ERROR)
  {
    long ipLastErr;
    ipLastErr = IpGetLastSocketError(gSocket);
    if (ipLastErr==WSA_IO_PENDING)
    {
      // The receive operation is performed asynchronously
    }
    else
    {
      Write("TcpReceive: operation failed (IpGetLastSocketError=%d)", ipLastErr);
      TCPClose(gSocket);
      gSocket = INVALID_SOCKET;
    }
  }
  else
  {
    Write("TcpReceive: operation failed (%d)", rc);
    TCPClose(gSocket);
    gSocket = INVALID_SOCKET;
  }
}

void OnTcpReceive( dword socket, long result, dword address, dword port, char buffer[], dword size)
{
  if (result==0)
  {
    if (size==0)
    {
      // Size of zero indicates that the socket was closed by the communication peer.
      Write("OnTcpReceive: socket closed by peer");
      TCPClose(gSocket);
      gSocket = INVALID_SOCKET;
    }
    else
    {
      // Sucessfully received some bytes over the TCP/IP connection.
      // Do something useful with the data ...
      // ... and continue receiving ...
      foo ();
    }
  }
  else
  {
    long ipLastErr;
    ipLastErr = IpGetLastSocketError(gSocket);
    Write("OnTcpReceive: operation failed (result=%d IpGetLastSocketError=%d)", result, ipLastErr);
    TCPClose(gSocket);
    gSocket = INVALID_SOCKET;
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
