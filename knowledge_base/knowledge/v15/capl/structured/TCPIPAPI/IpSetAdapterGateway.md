# IpSetAdapterGateway

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpSetAdapterGateway (dword ifIndex, dword ipv4address); // form 1
long IpSetAdapterGateway (dword ifIndex, byte ipv6Address[]); // form 2
long IpSetAdapterGateway (dword ifIndex, IP_Address address); // form 3
```

## Description

The function sets the default gateway address. There can only be one default gateway. An old default gateway address will be overwritten. The default gateway has to be in one of the subnets configured in the network stack, otherwise the network stack will not be able to find a route to the gateway. To remove the gateway, set the address 0.0.0.0 (IPv4) or :: (IPv6).

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. Although you set the default gateway on a defined interface, it is valid for the whole network stack. All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack. |
| ipv4address | The numerical IPv4 address for the gateway. |
| ipv6Address | The IPv6 address for the gateway in a 16 byte array. |
| address | IP address for the gateway. |

## Example

```c
variables
{
  UdpSocket gSocket;
}

on start
{
  ipSetAdapterGateway( 1, IP_Address(192.168.0.200) );
  gSocket = UdpSocket::Open( IP_Endpoint(192.168.0.17:40017) );

  // this send call to another sub-net will request the MAC address
  // of the gateway and sent the UDP packet to the MAC address of the gateway.
  gSocket.SendTo( IP_Endpoint(192.168.1.100:40100), "Hello", 5 );
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
