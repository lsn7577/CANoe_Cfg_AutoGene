# IP_Endpoint::SetToTCP

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Endpoint::SetToTCP();
```

## Description

Sets the transport protocol to TCP.

## Return Values

0: Success

## Example

```c
on start
{
  IP_Endpoint 192.168.1.1:4000 addr;
  addr.SetToTCP();
  if (addr.IsTCP())
  {
   write( "Is TCP endpoint" );
  }
}
```

## Availability

| Since Version |
|---|
