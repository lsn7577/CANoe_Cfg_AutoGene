# UdpConnect

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long udpConnect(dword socket, IP_Endpoint remoteEndpoint);
```

## Description

The function connects this socket to the given remote endpoint. After the socket is connected it is necessary to use UdpSend instead of UdpSendTo.

On Server side it is possible to connect to the remote endpoint when receiving data the first time on a socket. After that a new unconnected Socket can be created to wait for the next incoming udp connection (see example).

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| remoteEndpoint | The destination endpoint. IP address and port number must be specified. Example: IP_Endpoint( 192.168.1.1:40001 ) IP_Endpoint( [FC00::0001]:40001 ) |

## Example

```c
variables
{
  UdpSocket gSocket1;
  UdpSocket gSocket2;
  char gBuffer[1500];
}

on start
{
  gSocket1 = UdpSocket::Open( IP_Endpoint(0.0.0.0:0) );
  gSocket2 = UdpSocket::Open( IP_Endpoint(0.0.0.0:0) );
  gSocket1.Connect(IP_Endpoint(192.168.1.3:40002));
  gSocket2.Connect(IP_Endpoint(192.168.1.3:40002));
}

on key '1'
{
  // send on the connected socket
  SendCommand(gSocket1, "Request");

  // wait for response
  gSocket1.ReceiveFrom(gBuffer, elcount(gBuffer));
}

on key '2'
{
  // send on the connected socket
  SendCommand(gSocket2, "Request");

  // wait for response
  gSocket1.ReceiveFrom(gBuffer, elcount(gBuffer));
}

on key 'c'
{
  SendCommand(gSocket1, "End");
  gSocket1.Close();

  SendCommand(gSocket2, "End");
  gSocket1.Close();
}

SendCommand(UdpSocket socket, char command[])
{
  socket.Send(command, strlen(command));
}

OnUdpReceiveFrom(dword socket, long result, IP_Endpoint remoteEndpoint, char buffer[], dword size)
{
  // handle the response from the server here
}
variables
{
  // context to handle the state of the different connections
  struct connectionContext
  {
    int connectionNumber;
  };

  dword gListeningSocket;
  struct connectionContext connections[long];
  char gBuffer[1500];
  dword gConnectionCount;
}

on start
{
  gConnectionCount = 0;
  // open a socket and wait for the first data
  gListeningSocket = UdpOpen( IP_Endpoint(0.0.0.0:40002) );
  UdpReceiveFrom(gListeningSocket, gBuffer, elcount(gBuffer));
}

OnUdpReceiveFrom(dword socket, long result, IP_Endpoint remoteEndpoint, char buffer[], dword size)
{
  if(socket == gListeningSocket)
  {
    // create a context for this connection and open a new socket for the
    // next connection

    UdpConnect(socket, remoteEndpoint);
    connections[socket].connectionNumber = ++gConnectionCount;
    gListeningSocket = UdpOpen( IP_Endpoint(0.0.0.0:40002) );
    UdpReceiveFrom(gListeningSocket, gBuffer, elcount(gBuffer));
  }
  AnswerRequest(socket, buffer, size);
}

AnswerRequest(dword socket, char buffer[], dword size)
{
  char response[100];

  if(strncmp(buffer, "Request", size) == 0)
  {
    snprintf(response, elcount(response), "Response for connection #%d", connections[socket].connectionNumber);
    UdpSend(socket, response, strlen(response));
    UdpReceiveFrom(socket, gBuffer, elcount(gBuffer));
  }
  else if(strncmp(buffer, "End", size) == 0)
  {
    connections.remove(socket);
    UdpClose(socket);
  }
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
