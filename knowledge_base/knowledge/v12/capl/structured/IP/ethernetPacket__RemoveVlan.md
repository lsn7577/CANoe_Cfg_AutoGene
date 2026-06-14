# ethernetPacket::RemoveVlan

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.RemoveVlan(); // form 1
```

## Description

Removes a VLAN tag from an Ethernet packet.

To remove a specific VLAN tag from a double-tagged packet form 2 can be used.

## Example

```c
on ethernetPacket *
{
  if ((this.hasVlan()) && (this.msgChannel == 1))
  {
    ethernetPacket forwardPkt;

    forwardPkt = this;
    forwardPkt.msgChannel = 2;
    forwardPkt.RemoveVlan();

    output( forwardPkt );
  }
}
```

## Availability

| Since Version |
|---|
