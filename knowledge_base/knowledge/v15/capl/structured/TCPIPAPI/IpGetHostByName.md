# IpGetHostByName

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetHostByName(char hostname[],dword ipv4Address[], dword &count); // form 1
long IpGetHostByName(char hostname[],byte ipv6Address [][], dword &count); // form 2
long IpGetHostByName(char hostname[], IP_Address addresses[], dword &count ); // form 3
```

## Description

The function dissolves a host name in its IP address. The given host name first is searched in the CANoeSimulation Setup and then in the assigned database. If the name is not defined there it is determined via a DNS request by using the operating system stack. For this the operating system stack must be selected in the CANoeTCP/IP Stack configuration dialog. The result is then given back in the corresponding callback OnIpGetHostByName.

## Parameters

| Name | Description |
|---|---|
| hostname | The name of the host whose address should be determined. |
| ipv4Address | Array in which the determined IPv4 addresses are written. |
| ipv6Address | Array in which the determined IPv6 addresses are written. |
| count | On call: buffer size (only form 1-2) After call: Number of determined addresses |
| addresses | Array of IP_Address elements, which is filled with the IP addresses (IPv4 and IPv6) for the host. |

## Example

```c
//
// This example expects a node with the name ECU 1 in the
// simulation setup.
//

on start
{
  char addrStr[47];
  long result;
  dword count;
  dword loop;
  dword v4Addrs[10];
  byte  v6Addrs[10][16];

  //
  // get IPv4 addresses of node ECU 1
  //
  count = elCount(v4Addrs);
  result = IpGetHostByName("ECU 1", v4Addrs, count);
  if(result == 0)
  {
    write("IPv4 Addresses of Node ECU 1:");
    for(loop = 0; loop < count; loop++)
    {
      ipGetAddressAsString(v4Addrs[loop], addrStr, elcount(addrStr));
      write("%s", addrStr);
    }
  }

  //
  // get IPv6 addresses of node ECU 1
  //
  count = elCount(v6Addrs);
  result = IpGetHostByName("ECU 1", v6Addrs, count);
  if(result == 0)
  {
    write("IPv6 Addresses of Node ECU 1:");
    for(loop = 0; loop < count; loop++)
    {
      ipGetAddressAsString(v6Addrs[loop], addrStr, elcount(addrStr));
      write("%s", addrStr);
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 SP4: form 1-2 12.0: form 3 | 8.5 SP4: form 1-2 12.0: form 3 | 13.0 | 13.0: form 3 | — | 2.0 SP3: form 1-2 4.0: form 3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
