# IpGetAdapterAddress

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterAddress( dword ifIndex, dword ipv4address[],dword ipv4AddressSize); // form 1
long IpGetAdapterAddress( dword ifIndex, byte ipv6Addresses[][], dword ipv6AddressesSize); // form 2
long IpGetAdapterAddress( dword ifIndex, IP_Address addresses[], dword &count ); // form 3
```

## Description

The function retrieves the addresses associated with a network interface. The interface is specified by it's 1-based index in the list of network interfaces, i.e. the first interface has index 1.

All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. |
| ipv4address | The array used to store the numerical IPv4 addresses. |
| ipv6Addresses | The array used to store the IPv6 addresses as 16 byte arrays. |
| ipv4AddressSize | The size of the address array. |
| ipv6AddressSize | The size of the address array. |
| count | Number of IP address, which were copied to addresses. |
| addresses | Array of IP_Address elements, which is filled with the configured IP addresses of the specified interface. |

## Example

```c
on start
{
  IP_Address addresses[10];
  dword addressesCount;
  IP_Address addrMasks[10];
  dword addrMasksCount;
  long addrIdx;
  long ifIdx;

  write( "IP Configuration" );

  for( ifIdx = 1; ifIdx <= ipGetAdapterCount(); ifIdx++)
  {
    ipGetAdapterAddress( ifIdx, addresses, addressesCount );
    ipGetAdapterMask( ifIdx, addrMasks, addrMasksCount );
    for( addrIdx = 0; addrIdx < addressesCount; addrIdx++ )
    {
      char addrStr[30];
      char maskStr[30];
      addresses[addrIdx].PrintAddressToString( addrStr );
      addrMasks[addrIdx].PrintAddressToString( maskStr );

      write( "  %d. %s | %s", addrIdx+1, addrStr, maskStr );
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
