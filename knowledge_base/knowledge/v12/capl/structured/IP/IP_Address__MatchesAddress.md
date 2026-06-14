# IP_Address::MatchesAddress

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Address::MatchesAddress (IP_Address ipAddr); // form 1
```

## Description

Compares two addresses whereas wildcards matches always. If no address type is set or the address is set to 0.0.0.0 (IPv4) or ::0 (IPv6) this is considered as wildcard.

With form 2 only the network address of the IP address will be considered.

## Return Values

0: No match

## Example

```c
on start
{
  IP_Address 192.168.1.1 addr1;
  IP_Address 192.168.1.2 addr2;
  if (addr1 == addr2)
  {
    write( "Addresses are equal!" );
  }
  else
  {
    write( "Addresses are not equal!" );
  }
}
```

## Availability

| Since Version |
|---|
