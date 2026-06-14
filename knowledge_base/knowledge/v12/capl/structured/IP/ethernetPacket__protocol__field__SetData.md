# ethernetPacket::protocol::field::SetData

> Category: `IP` | Type: `function`

## Syntax

```c
word ethernetPacket.<protocol>.<field>.SetData( word offset, char[]data, word length );
```

## Description

Sets payload data of a protocol within an Ethernet packet.

The length of the protocol field is not changed. If the source data is larger than the protocol field, the data is truncated.

If <protocol> or <field> is not available in the packet, no data is set and 0 is returned.

## Return Values

Number of bytes copied to the Ethernet packet.

## Example

```c
ethernetPacket pkt;
byte ipv6AddrData[16];

// initialize packet with IPv6 and UDP protocols
pkt.ipv6.Init();
pkt.udp.Init();

// set IPv6 addresses
ipGetAddressAsArray( "FC00::01", ipv6AddrData );
pkt.ipv6.source.SetData( 0, ipv6AddrData, elcount(ipv6AddrData) );

ipGetAddressAsArray( "FC00::02", ipv6AddrData );
pkt.ipv6.destination.SetData( 0, ipv6AddrData, elcount(ipv6AddrData) );

// set UDP ports
pkt.udp.source      = 40001;
pkt.udp.destination = 40002;

// set UDP payload
pkt.udp.SetData( 0, "Hello", 5 );

// calculate UDP and IPv6 checksum and send Ethernet packet
pkt.CompletePacket();
output( pkt );
```

## Availability

| Since Version |
|---|
