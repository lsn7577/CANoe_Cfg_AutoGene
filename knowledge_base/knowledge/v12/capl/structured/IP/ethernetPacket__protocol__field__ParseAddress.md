# ethernetPacket::protocol::field::ParseAddress

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.<protocol>.<field>.ParseAddress( char addressAsString[] );
```

## Description

Sets the protocol field, which has type IPv4 or IPv6 address.

The address must be given in

The method is only available for IPv4 or IPv6 address fields.

## Return Values

0: Success

## Example

```c
ethernetPacket pkt;

pkt.udp.Init();

pkt.ipv4.source.ParseAddress( "192.168.1.1" );
pkt.ipv4.destination.ParseAddress( "255.255.255.255" );
ethernetPacket pkt;

pkt.ipv6.Init();
pkt.udp.Init();

pkt.ipv6.source.ParseAddress( "FC01::1" );
pkt.ipv6.destination.ParseAddress( "FF00::1" );
```

## Availability

| Since Version |
|---|
