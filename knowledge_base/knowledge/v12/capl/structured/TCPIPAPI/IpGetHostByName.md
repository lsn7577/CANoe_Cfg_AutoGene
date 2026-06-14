# IpGetHostByName

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetHostByName(char hostname[],dword ipv4Address[], dword &count); // form 1
```

## Description

The function dissolves a host name in its IP address. The given host name first is searched in the CANoe Simulation Setup and then in the assigned database. If the name is not defined there it is determined via a DNS request by using the operating system stack. For this the operating system stack must be selected in the CANoe TCP/IP Stack configuration dialog. The result is then given back in the corresponding callback OnIpGetHostByName.

## Return Values

0: The function completed successfully.

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

| Since Version |
|---|
