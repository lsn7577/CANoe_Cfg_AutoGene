# ethernetPacket::GetVlan

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.GetVlan(word &tpid, word &tci); // form 1
```

## Description

Returns the VLAN tag, if the Ethernet packet contains a VLAN tag.For double-tagged VLAN form 2 can be used to access a specific VLAN tag.

## Return Values

0: Success

## Example

```c
on ethernetPacket *
{
  if (this.hasVlan())
  {
    word tpid, tci;

    if (this.GetVlan( tpid, tci ) == 0)
    {
      write( "Received Ethernet packet with VLAN TPID 0x%X TCI 0x%X", tpid, tci );
    }
  }
}
```

## Availability

| Since Version |
|---|
