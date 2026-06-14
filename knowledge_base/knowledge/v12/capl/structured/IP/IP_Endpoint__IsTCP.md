# IP_Endpoint::IsTCP

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Endpoint::IsTCP();
```

## Description

Checks if the current transport protocol of this endpoint is TCP.

## Return Values

Returns 1 if the current transport protocol of this endpoint is TCP.

## Example

```c
on start
{
  IP_Endpoint UDP:192.168.1.1:4000 addr;
  if (addr.IsUDP())
  {
    write( "Is UDP endpoint" );
  }
  else if (addr.IsTCP())
  {
    write( "Is TCP endpoint" );
  }
}
```

## Availability

| Since Version |
|---|
