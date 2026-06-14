# IpGetAddressAsNumber

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword IpGetAddressAsNumber( char address[]);
```

## Description

The function converts an IPv4 address string in dot notation to it's numerical value in network-byte order.

## Return Values

4294967295 (0xFFFFFFF, the equivalent of "255.255.255.255"): The specified address string was invalid.

## Example

```c
on start
{
  const dword IPV4_STR_SIZE = 16;    // IPv4 string size
  char ipv4AddrStr[IPV4_STR_SIZE] = "129.168.111.222";

  write("Converting IPv4 Address %s to numerical value => 0x%x", ipv4AddrStr, IpGetAddressAsNumber(ipv4AddrStr));
}
```

## Availability

| Since Version |
|---|
