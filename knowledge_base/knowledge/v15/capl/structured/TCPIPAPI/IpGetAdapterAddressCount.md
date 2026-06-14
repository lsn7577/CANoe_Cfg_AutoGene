# IpGetAdapterAddressCount

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterAddressCount( dword ifIndex, dword addressFamily);
```

## Description

The function returns the count of addresses belonging to the given address family which are assigned to the adapter with the given index.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack. |
| addressFamily | The address family of the addresses, the address count will be returned. Possible values are:AF_INET (2): IPv4 address familyAF_INET6 (28): IPv6 address family |

## Return Values

The count of addresses of the given address family will be returned.

## Example

```c
on start
{
  const dword AF_INET = 2;   // IPv4 adapter family
  const dword AF_INET6 = 28; // IPv6 adapter family
  dword ifIdx;               // interface index
  long ipv4AdrCount;         // variable for count of all ipv4 addresses of first adapter
  long ipv6AdrCount;         // variable for count of all ipv6 addresses of first adapter

  for (ifIdx = 1; ifIdx <= IpGetAdapterCount(); ifIdx++)
  {
    ipv4AdrCount = IpGetAdapterAddressCount( ifIdx, AF_INET );
    if (ipv4AdrCount != -1)
    {
      write("IpGetAdapterAddressCount: Adapter with index %d has %d IPv4 addresses assigned.", ifIdx, ipv4AdrCount);
    }
    else
    {
      writeLineEx(1, 3, "IpGetAdapterAddressCount: Error: The function call failed. Invalid ifIndex given for ipv4.");
    }

    ipv6AdrCount = IpGetAdapterAddressCount( ifIdx, AF_INET6 );
    if (ipv6AdrCount != -1)
    {
      write("IpGetAdapterAddressCount: Adapter with index %d has %d IPv6 addresses assigned.", ifIdx, ipv6AdrCount);
    }
    else
    {
      writeLineEx(1, 3, "IpGetAdapterAddressCount: Error: The function call failed. Invalid ifIndex given for ipv6.");
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.2 SP2 | 13.0 | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
