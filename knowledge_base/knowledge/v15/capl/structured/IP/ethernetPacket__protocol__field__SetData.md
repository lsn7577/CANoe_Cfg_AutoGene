# ethernetPacket::protocol::field::SetData

> Category: `IP` | Type: `method`

## Syntax

```c
word ethernetPacket.<protocol>.<field>.SetData( word offset, char[]data, word length ); // from 1
word ethernetPacket.<protocol>.<field>.SetData( word offset, byte[]data, word length ); // form 2
word ethernetPacket.<protocol>.<field>.SetData( word offset, struct * data); // from 3
word ethernetPacket.<protocol>.<field>.SetData( word offset, sysvarStruct data); // from 4
```

## Description

Sets payload data of a protocol within an Ethernet packet.

The length of the protocol field is not changed. If the source data is larger than the protocol field, the data is truncated.

If <protocol> or <field> is not available in the packet, no data is set and 0 is returned.

## Parameters

| Name | Description |
|---|---|
| data | buffer where the data is copied from. |
| length | Number of bytes to copy to the protocol field data. |
| offset | Byte offset in the protocol field data where it starts to copy data. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 SP3 | 11.0 SP3 | 13.0 | — | — | 3.0 SP3 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
