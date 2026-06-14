# ethernetPacket::SetVlan

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.SetVlan(word tpid,word tci); // form 1
```

## Description

Sets the VLAN tag of an Ethernet packet. If the packets does not contain a VLAN tag, a new VLAN tag is added.

For double-tagged VLAN form 2 can be used.

## Return Values

0: Success

## Example

```c
on key '1'
{
  ethernetPacket pkt;

  pkt.SetVlan( 0x8100, 0x5123 );

  output( pkt );
}

on key '2'
{
  ethernetPacket pkt;

  // double tagged VLAN
  pkt.SetVlan( 0, 0x8100, 0x5123 );
  pkt.SetVlan( 1, 0x88A8, 0x6456 );

  output( pkt );
}
```

## Availability

| Since Version |
|---|
