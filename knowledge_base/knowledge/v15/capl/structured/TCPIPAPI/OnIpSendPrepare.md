# OnIpSendPrepare

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long OnIpSendPrepare( dword socket, ethernetPacket * packet);
```

## Description

If the CAPL program implements this callback it is called right before a packet will be sent by the TCP/IP stack.

It is possible to manipulate the content of the packet or to block the sending of the package on the bus.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| packet | The Ethernet packet which will be send. |

## Example

```c
variables
{
  const dword INVALID_SOCKET = ~0;
  DWORD gUdpSocket;
}

on start
{
  dword result;
  char data[100] = "Hello world";
  // open udp socket
  gUdpSocket = UdpOpen(0, 0);
  if(gUdpSocket == INVALID_SOCKET)
  {
    writeLineEx(1,3,"%BASE_FILE_NAME%: Failed to open udp socket. Error: %d", IpGetLastError());
  }
  // send data on udp socket
  result = UdpSendTo(gUdpSocket, ipGetAddressAsNumber("192.168.1.1"), 21, data, strlen(data));
  if(result != 0)
  {
    writeLineEx(1,3,"%BASE_FILE_NAME%: Failed to send data on udp socket. Error: %d", IpGetLastSocketError(gUdpSocket));
  }
}

long OnIpSendPrepare( dword socket, ethernetPacket * packet)
{
  if(socket == gUdpSocket)
  {
    // change destination MAC id to broadcast
    packet.destination = ethGetMacAddressAsNumber("FF:FF:FF:FF:FF:FF");
    // change ip destination address to broadcast address.
    // Since this address is covered by the IP checksum this will
    // lead to a checksum error.
    packet.dword(16) = ipGetAddressAsNumber("255.255.255.255");
  }
  return 1; // send packet
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 SP3 | 8.5 SP3 | 13.0 | — | — | 2.0 SP2 |
| Restricted To | IP | IP | IP | — | — | IP |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
