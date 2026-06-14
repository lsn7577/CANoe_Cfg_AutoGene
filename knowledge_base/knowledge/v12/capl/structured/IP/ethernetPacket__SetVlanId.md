# ethernetPacket::SetVlanId

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.SetVlanId(word vlanId); // form 1
```

## Description

Sets the VLAN ID of an Ethernet packet. If the packets does not contain a VLAN tag, a new VLAN tag is added.

For double-tagged VLAN form 2 can be used.

## Return Values

0: Success

## Example

```c
on key '1'
{
  ethernetPacket pkt;

  pkt.SetVlanId( 10 );
  pkt.SetVlanPriority( 1 );

  output( pkt );
}

on key '2'
{
  ethernetPacket pkt;

  // double tagged VLAN
  pkt.SetVlanId( 0, 10 );
  pkt.SetVlanPriority( 0, 1 );
  pkt.SetVlanId( 1, 20 );
  pkt.SetVlanPriority( 1, 2 );

  output( pkt );
}
```

## Availability

| Since Version |
|---|
