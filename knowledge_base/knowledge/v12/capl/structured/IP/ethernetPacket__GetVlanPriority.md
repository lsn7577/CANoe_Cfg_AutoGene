# ethernetPacket::GetVlanPriority

> Category: `IP` | Type: `function`

## Syntax

```c
dword ethernetPacket.GetVlanPriority(); // form 1
```

## Description

Returns the VLAN priority, if the Ethernet packet contains a VLAN tag.For double-tagged VLAN form 2 can be used to access a specific VLAN priority.

## Return Values

ID of the VLAN or 0xFFFF if no VLAN is available.

## Example

```c
on ethernetPacket *
{
  if (this.hasVlan())
  {
    word vlanPrio;

    vlanPrio = this.GetVlanPriority();

    write( "Received Ethernet packet with VLAN priority %d", vlanPrio );
  }
}
```

## Availability

| Since Version |
|---|
