# ethernetPacket::protocol::Init

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.<protocol>.Init();
```

## Description

Initialize the protocol within an Ethernet packet. It appends the protocol, if it is not already contained in the packet and initialized the protocol header with default values. If a protocol requires other underlaying protocols, it will add these protocols too, i.e. if the UDP protocol is initialized it also adds an IPv4 protocol header by default. If a specific protocol stack is required, the Init() function can be called for every protocol from the lower protocols to the upper protocols, i.e. if UDP over IPv6 is required, first initialize IPv6 and then UDP. Higher protocols than the one which is initialized, will be removed.

## Return Values

0: Success

## Example

```c
ethernetPacket pkt;
// initialize packet with IPv4 and UDP protocols
pkt.udp.Init();
// set IPv4 addresses
pkt.ipv4.source.ParseAddress( "192.168.1.1" );
pkt.ipv4.destination.ParseAddress ( "192.168.1.255" );
// set UDP ports
pkt.udp.source      = 40001;
pkt.udp.destination = 40002;
// set UDP payload
pkt.udp.SetData( 0, "Hello", 5 );
// calculate UDP and IPv4 checksum and send Ethernet packet
pkt.CompletePacket();
output( pkt );
ethernetPacket pkt;

// initialize packet with IPv6 and UDP protocols
pkt.ipv6.Init();
pkt.udp.Init();

// set IPv6 addresses
pkt.ipv6.source.ParseAddress("FC00::01" );
pkt.ipv6.destination.ParseAddress("FC00::02",  );

// set UDP ports
pkt.udp.source      = 40001;
pkt.udp.destination = 40002;

// set UDP payload
pkt.udp.SetData( 0, "Hello", 5 );

// calculate UDP and IPv4 checksum and send Ethernet packet
pkt.CompletePacket();
output( pkt );
```

## Availability

| Since Version |
|---|
