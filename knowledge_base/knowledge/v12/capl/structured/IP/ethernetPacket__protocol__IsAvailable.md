# ethernetPacket::protocol::IsAvailable

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.<protocol>.IsAvailable();
```

## Description

Checks if a protocol or protocol field is contained in the Ethernet packet.

## Return Values

1: Ethernet packet contains the protocol

## Example

```c
on ethernetPacket *
{
  if (this.udp.IsAvailable())
  {
  write( "Packet has UDP protocol with port %d to %d!", this.udp.source, this.udp.destination );
  }
}
```

## Availability

| Since Version |
|---|
