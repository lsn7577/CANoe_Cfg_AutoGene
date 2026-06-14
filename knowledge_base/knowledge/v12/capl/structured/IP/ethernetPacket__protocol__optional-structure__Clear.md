# ethernetPacket::protocol::optional-structure::Clear

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.<protocol>.<optional-structure>.Clear();
```

## Description

Removes a protocol option from the Ethernet packet.

## Return Values

0: Success

## Example

```c
on ethernetPacket msgChannel1.*
{
  if (this.ipv6.fragment.IsAvailable()
  {
    ethernetPacket pkt;

    // copy packet
    pkt            = this;
    pkt.msgChannel = 2;

    // remove option fragment
    pkt.ipv6.fragment.Clear();

    // recalculate checksums and output packet
    pkt.CompletePacket();
    output( pkt )
  }
}
```

## Availability

| Since Version |
|---|
