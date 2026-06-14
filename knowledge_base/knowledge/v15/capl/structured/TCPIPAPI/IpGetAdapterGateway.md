# IpGetAdapterGateway

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterGateway( dword ifIndex, dword& ipv4address); // form 1
long IpGetAdapterGateway( dword ifIndex, byte ipv6Address[]); // form 2
long IpGetAdapterGateway( dword ifIndex, dword addressFamily , IP_Address address); // form 3
```

## Description

The function retrieves the default gateway address associated with the specified network interface.

Gateway information is not yet available before the start of the measurement (on pre-start). Rather it is first available at the start of the measurement (on start) as soon as the stack has been completely initialized.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack. |
| ipv4address | The returned numerical gateway IPv4 address. |
| ipv6Address | The local IPv6 address in a 16 byte array. |
| count | The size of the address array. |
| addressFamily | The address family of the addresses, the address count will be returned. Possible values are: 0: IPv4 address family, if available, else IPv6 family 2: IPv4 address family 28: IPv6 address family |
| address | IP_Address variable where the address is copied to. |

## Example

```c
on start
{
  long ifIdx;
  for( ifIdx = 1; ifIdx <= ipGetAdapterCount(); ifIdx++)
  {
    ip_Address gatewayAddress;
    if (ipGetAdapterGateway( ifIdx, 0, gatewayAddress ) == 0)
    {
      char gatewayStr[30];
      gatewayAddress.PrintAddressToString( gatewayStr );
      write( "%d. Adapter Gateway Address: %s", ifIdx, gatewayStr );
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: form 1-2 12.0: form 3 | 7.0: form 1-2 12.0: form 3 | 13.0 | 13.0: form 3 | — | 2.0 SP2: form 1-2 4.0: form 3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
