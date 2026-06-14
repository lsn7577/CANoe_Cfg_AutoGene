# IP_Address::IsIPv4Address

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Address::IsIPv4Address();
```

## Description

Checks if the current address is an IPv4 address.

## Return Values

Returns 1 if the object currently represents an IPv4 address.

## Example

```c
on start
{
  DoSomething( IP_Address(192.168.1.2) );
}

void DoSomething( IP_Address addr )
{
  if (addr.IsIPv4Address())
  {
    // ...
  }
  else if (addr.IsIPv6Address())
  {
    // ...
  }
}
```

## Availability

| Since Version |
|---|
