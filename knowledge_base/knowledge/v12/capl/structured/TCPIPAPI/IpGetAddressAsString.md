# IpGetAddressAsString

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAddressAsString( dword numericAddress, char address[], dword count);
```

## Description

The function converts a numeric address in host-byte order (little endian) to an address string in dot notation as in "192.168.0.10". For IPv6 the address string has to contain a string in colon notation as in "1234:5678:9ABC:DEF1:2345:6789:ABCD:EF12"

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  const dword IPV4_STR_SIZE = 16;   // IPv4 string size
  const dword IPV6_STR_SIZE = 40;   // IPv6 string size
  dword ipv4Addr = 0xde6fa881;      // an IPv4Addr (192.168.111.222)
  char ipv4AddrStr[IPV4_STR_SIZE];  // an IPv4Addr string buffer
  char ipv6AddrStr[IPV6_STR_SIZE];  // an IPv6Addr string buffer
  long result;                      // function result;
  byte ipv6Addr[16] = {0x20,0x01,0x0D,0xB8,0x85,0xA3,0x08,0xD3,0x13,0x19,0x8A,0x2E,0x03,0x70,0x73,0x44}; // an IPv6 Addr (2001:DB8:85A3:8D3:1319:8A2E:370:7344)

  result = IpGetAddressAsString( ipv4Addr, ipv4AddrStr, elcount(ipv4AddrStr) );
  if (result == 0)
  {
    write("IpGetAddressAsString: Address 0x%x => %s", ipv4Addr, ipv4AddrStr);
  }
  else
  {
    writeLineEx(1, 3, "IpGetAddressAsString: Error %d", result);
  }

  result = IpGetAddressAsString( ipv6Addr, ipv6AddrStr, elcount(ipv6AddrStr) );
  if (result == 0)
  {
    write("IpGetAddressAsString: IPv6 address bytes => %s", ipv6AddrStr);
  }
  else
  {
    writeLineEx(1, 3, "IpGetAddressAsString: Error %d", result);
  }
}
```

## Availability

| Since Version |
|---|
