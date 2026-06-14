# ethernetPacket::GetVlanId

> Category: `IP` | Type: `function`

## Syntax

```c
dword ethernetPacket.GetVlanId(); // form 1
```

## Description

Returns the VLAN ID, if the Ethernet packet contains a VLAN tag.For double-tagged VLAN form 2 can be used to access a specific VLAN ID.

## Return Values

ID of the VLAN or 0xFFFF if no VLAN is available.

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
