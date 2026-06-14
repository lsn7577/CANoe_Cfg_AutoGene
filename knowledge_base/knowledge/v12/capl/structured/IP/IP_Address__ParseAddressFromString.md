# IP_Address::ParseAddressFromString

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Address::ParseAddressFromString(char ipAddr[]);
```

## Description

Converts the character string to an IPv4 or IPv6 address and sets this address to the IP address value.

## Return Values

0: Success

## Example

```c
on start
{
  IP_Address addr;
  if (addr.ParseAddressFromString( "192.168.1.1" ) == 0)
  {
    // do something with addr
  }
}
```

## Availability

| Since Version |
|---|
