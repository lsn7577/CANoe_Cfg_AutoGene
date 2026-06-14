# IpRemoveAdapterAddress

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpRemoveAdapterAddress (dword ifIndex, dword ipv4address, dword ipv4mask); // form 1
long IpRemoveAdapterAddress (dword ifIndex, byte ipv6Address[], dword prefix); // form 2
long IpRemoveAdapterAddress (dword ifIndex, IP_Address address, dword prefix); // form 3
```

## Description

The function removes an address from the network interface with the given index.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack. |
| ipv4address | The numerical IPv4 address to remove from the interface. |
| ipv6Address | The IPv6 address to remove from the interface in a 16 byte array. |
| ipv4mask | The IPv4 network mask in network byte order. |
| prefix | The IPv6 prefix for the given IPv6 address. |
| address | IP Adress to add to the interface. |

## Example

```c
variables
{
  UdpSocket gSocket;
}

on start
{
  ipAddAdapterAddress( 1, IP_Address( 192.168.0.116 ), 24 );
  gSocket = UdpSocket::Open( IP_Endpoint(192.168.0.116:40016) );
  gSocket.SendTo( IP_Endpoint(192.168.0.255:40255), "Hello", 5 );
}

on preStop
{
  ipRemoveAdapterAddress( 1, IP_Address( 192.168.0.116 ), 24 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: form 1-2 12.0: form 3 | 8.1: form 1-2 12.0: form 3 | 13.0 | 13.0: form 3 | — | 2.0 SP2: form 1-2 4.0: form 3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
