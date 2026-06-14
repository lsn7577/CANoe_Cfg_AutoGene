# IP_Endpoint::SetTransportProtocolToUnknown

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Endpoint::SetTransportProtocolToUnknown();
```

## Description

Invalidates the transport protocol.

## Return Values

0: Success

## Example

```c
on start
{
  IP_Endpoint UDP:192.168.1.1:4000 addr;
  addr.SetTransportProtocolToUnknown();
  if (addr.IsTCP())
  {
    write( "Is TCP endpoint" );
  }
  else if (addr.IsUDP())
  {
    write( "Is UDP endpoint" );
  }
  else
  {
    write( "No transport protocol specified for endpoint" );
  }
}
```

## Availability

| Since Version |
|---|
