# IP_Address::IsMulticast

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Address::IsMulticast();
```

## Description

Checks if the current address is a multicast address.

## Return Values

Returns 1 if the object’s address value is a multicast address.

## Example

```c
on start
{
  DoSomething( IP_Address(239.0.0.1) );
}

void DoSomething( IP_Address addr )
{
  if (addr.IsMulticast())
  {
    // ...
  }
  else if (addr.IsBroadcast())
  {
    // ...
  }
}
```

## Availability

| Since Version |
|---|
