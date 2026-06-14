# TcpGetRemoteEndpoint

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
TcpGetRemoteEndpoint( dword socket, IP_Endpoint remoteEndpoint );
```

## Description

The function retrieves the remote endpoint of the specified connected socket.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| remoteEndpoint | IP_Endpoint which returns the IP endpoint. |

## Example

```c
variables
{
  TcpSocket gListenSocket;
  TcpSocket gConnectionSocket;
  char gRxBuffer[1000];
}

on start
{
  gListenSocket = TcpSocket::Open( IP_Endpoint(0.0.0.0:40004) );

  gListenSocket.Listen();
}

OnTcpListen( TcpSocket socket, long result)
{
  if (result == 0)
  {
    gConnectionSocket = TcpSocket::Accept( gListenSocket );

    {
      IP_Endpoint localEndpoint;
      IP_Endpoint remoteEndpoint;
      char localAddrStr[100];
      char remoteAddrStr[100];

      gConnectionSocket.GetSocketName( localEndpoint );
      gConnectionSocket.GetRemoteEndpoint( remoteEndpoint );

      localEndpoint.PrintEndpointToString( localAddrStr );
      remoteEndpoint.PrintEndpointToString( remoteAddrStr );
      write( "Accepted local %s, remote %s", localAddrStr, remoteAddrStr );
    }

    gConnectionSocket.Receive( gRxBuffer, elcount( gRxBuffer) );
  }
}

OnTcpReceive( TcpSocket socket, long result, IP_Endpoint remoteEndpoint, char buffer[], dword size )
{
  if (result == 0)
  {
    write( "Received: %s", buffer );

    gConnectionSocket.Send( "Response", 8 );

    gConnectionSocket.Receive( gRxBuffer, elcount( gRxBuffer) );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | 13.0 | — | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
