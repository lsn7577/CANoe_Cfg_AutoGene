# TcpConnect

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long TcpConnect( dword socket, dword address, dword port); // form 1
long TcpConnect( dword socket, byte ipv6Address[], dword port); // form 2
long TcpConnect( dword socket, IP_Endpoint remoteEndpoint ); // form 3
```

## Description

The function establishes a connection with the specified location.

Use IpGetLastSocketError to get a more specific error code. The specific error code is WSAWOULDBLOCK (10035), is no “real” error, but just confirms the non-blocking socket behavior. A real connection error is different from error 10035.

The CAPL callback OnTcpConnect will be called on completion (successful or not), provided it is implemented in the same CAPL program.

On the remote station OnTcpListen is called up, which accepts the connection with TcpAccept.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| address | The numerical IPv4 address of the destination. |
| ipv6Address | The numerical IPv6 address of the destination in a 16 byte array. |
| port | The port of the destination in host-byte order. |
| remoteEndpoint | The destination endpoint. IP address and port number must be specified. Example: IP_Endpoint( 192.168.1.1:40001 ) IP_Endpoint( [FC00::0001]:40001 ) |

## Example

```c
// ---------------------------------------------------
// connect a client...
// ---------------------------------------------------
void clientConnect()
{
  dword result;
  clientSocket = TcpOpen( 0, 0 );
  if (clientSocket != INVALID_SOCKET)
  {
    result = TcpConnect( clientSocket, ipv4Addr[0], listenPort );
    if ( result == -1)
    {
      result = IpGetLastSocketError(clientSocket);
      if ( result != 10035)
      {
        writeLineEx( 1, 3, " [ TcpConnect for client failed with error %d ]", result );
      }
    }
    else
    {
      writeLineEx(1, 3, " [ TcpConnect error %d ]", result);
    };
  }
  else
  {
    writeLineEx(1, 3, " [ TcpOpen: FAILED. ]");
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: function/method 1-2 12.0: function/method 3 | 7.0: function 1-2 7.0 SP5: method 1-2 12.0: function/method 3 | 13.0 | 13.0: form 3 | — | 2.0 SP2: function/method 1-2 4.0: function/method 3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
