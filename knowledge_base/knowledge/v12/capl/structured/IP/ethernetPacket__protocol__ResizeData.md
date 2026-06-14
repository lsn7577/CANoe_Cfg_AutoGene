# ethernetPacket::protocol::ResizeData

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.<protocol>.ResizeData( word newLength );
```

## Description

Resizes the payload of a protocol within an Ethernet packet.

If the newLength is greater than the length of the Ethernet packet, the Ethernet packet is enlarged.

If <protocol> is not available in the packet, an error is returned.

## Return Values

0: Success

## Example

```c
word i;
ethernetPacket pkt;

pkt.udp.Init();
pkt.udp.ResizeData( 200 );

for (i = 0; i < 200; i++ )
{
  pkt.udp.Byte(i) = 0;
}

pkt.CompletePacket();
output( pkt );
```

## Availability

| Since Version |
|---|
