# ethernetPacket::HasVlan

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.HasVlan(); // form 1
```

## Description

Returns number of VLAN tags.

## Return Values

Number of VLAN tags

## Example

```c
on ethernetPacket *
{
  if (this.hasVlan())
  {
    word vlanId;

    vlanId = this.GetVlanId();

    write( "Received Ethernet packet with VLAN ID %d", vlanId );
  }
}
```

## Availability

| Since Version |
|---|
