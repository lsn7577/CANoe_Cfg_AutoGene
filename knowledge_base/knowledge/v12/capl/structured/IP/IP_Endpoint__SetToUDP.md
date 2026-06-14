# IP_Endpoint::SetToUDP

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Endpoint::SetToUDP();
```

## Description

Sets the transport protocol to UDP.

## Return Values

0: Success

## Example

```c
on start
{
  IP_Endpoint 192.168.1.1:4000 addr;
  addr.SetToUDP();
  if (addr.IsUDP())
  {
   write( "Is UDP endpoint" );
  }
}
```

## Availability

| Since Version |
|---|
