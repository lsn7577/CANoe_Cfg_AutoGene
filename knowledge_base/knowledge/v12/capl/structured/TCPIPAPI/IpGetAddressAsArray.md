# IpGetAddressAsArray

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword IpGetAddressAsArray( char address[], byte ipv6Address[]);
```

## Description

The function converts an address string in colon notation to a 16 byte array with the address bytes in network order.

## Return Values

0xFFFFFF: The specified address string was invalid.

## Example

```c
on start
{
  const dword IPV6_STR_SIZE = 40; // IPv6 string size
  int i;                          // loop variable
  byte ipv6Addr[16];              // IPv6 address bytes.
  dword result;                   // function result

  char ipv6AddrStr[IPV6_STR_SIZE] = "2001:DB8:85A3:8D3:1319:8A2E:370:7344";

  write("Converting IPv6 Address %s to bytes...", ipv6AddrStr);

  result = IpGetAddressAsArray( ipv6AddrStr, ipv6Addr );
  if (result == 0)
  {
    // success...
    write("IpGetAddressAsArray: returned array with IPv6 bytes:");
    for ( i=0; i<16; i++)
    {
      write("Byte %.2d = 0x%.2x", i, ipv6Addr[i]);
    }
  }
  else
  {
    writeLineEx(1, 3, "IpGetAddressAsArray: The specified address string was invalid.");
  }
}
```

## Availability

| Since Version |
|---|
