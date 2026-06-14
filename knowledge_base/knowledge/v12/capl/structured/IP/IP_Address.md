# IP_Address

> Category: `IP` | Type: `function`

## Syntax

```c
IP_Address <addr> <var name>; // form 1
```

## Description

Initializes a variable of type IP_Address with a concrete IP address (form 1) or without an IP Address (form 2).

## Example

```c
variables
{
  IP_Address 192.168.0.1 ipv4Addr;
  IP_Address ff::1       ipv6Addr;
  IP_Address [ff::2]     ipv6Addr2;
  IP_Address 0.0.0.0     ipv4AnyAddr;
  IP_Address ::          ipv6AnyAddr;
}
on start
{
  IP_Address addr;
  addr = IP_Address(192.168.1.1);
  // ... do something with addr
}
on start
{
  DoSomething( IP_Address(192.168.1.1) );
}

void DoSomething( IP_Address addr )
{
  // ... do something with addr
}
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

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| IPv4Address Accesses the IPv4 address’ value. The byte order is network byte order. | dword | — |
| ScopeID ScopeID for an IPv6 address. | dword | — |
