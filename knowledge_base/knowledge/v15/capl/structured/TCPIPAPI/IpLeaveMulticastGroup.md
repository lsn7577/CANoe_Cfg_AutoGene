# IpLeaveMulticastGroup

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpLeaveMulticastGroup( dword socket, dword ifIndex, dword ipv4address ); // form 1
long IpLeaveMulticastGroup( dword socket, dword ifIndex, byte ipv6Address[] ); // form 2
long IpLeaveMulticastGroup( dword socket, dword ifIndex, IP_Address multicastAddress ); // form 3
```

## Description

Leaves a previously joined multicast group on the given socket.

After that no multicast messages are received anymore.

To receive multicast messages, the multicast group has to be joined with IpJoinMulticastGroup before.

Before multicast messages can be sent, IpSetMulticastInterface has to be called before.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| ifIndex | The 1-based network interface index. All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack. |
| ipv4address | The numerical IPv4 address of the destination. |
| ipv6Address | The local IPv6 address in a 16 byte array. |
| multicastAddress | The IP multicast address of the destination. |

## Example

```c
variables
{
  UdpSocket gSocket;
}

on start
{
  gSocket = UdpSocket::Open( IP_Endpoint(0.0.0.0:40001) );
  gSocket.JoinMulticastGroup( 1, IP_Address(239.0.0.123) );
}

on key '2'
{
  gSocket.LeaveMulticastGroup( 1, IP_Address(239.0.0.123) );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: form 1-2 12.0: form 3 | 8.2: form 1-2 12.0: form 3 | 13.0 | 13.0: form 3 | — | 2.0 SP2: form 1-2 4.0: form 3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
