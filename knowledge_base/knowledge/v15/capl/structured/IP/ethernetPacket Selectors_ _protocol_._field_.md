# ethernetPacket Selectors: <protocol>.<field>

> Category: `IP` | Type: `notes`

## Description

byte ethernetPacket.<protocol>.<field>;

word ethernetPacket.<protocol>.<field>;

dword ethernetPacket.<protocol>.<field>;

qword ethernetPacket.<protocol>.<field>;

Read or write access to protocol fields.

See protocol overview for protocol and field designators.

If <protocol> or <field> is not contained in the packet, the measurement is stopped with a runtime error. ethernetPacket::<protocol>::IsAvailable and ethernetPacket::<protocol>::<field>::IsAvailable can be used to find out if the field is available.

The data type depends on the protocol field. The bit length is rounded up to next larger CAPL data type, i.e. a 4-bit protocol field will use byte and a 12 bit protocol field will use word.

This selector is available for protocol field of type integer. For protocol fields, which are not of type integer, the method GetData and SetData can be used.

—

| ethernetPacket pkt;// initialize packet with IPv4 and UDP protocolspkt.udp.Init();// set IPv4 addressespkt.ipv4.source.ParseAddress( "192.168.1.1" );pkt.ipv4.destination.ParseAddress ( "192.168.1.255" );// set UDP portspkt.udp.source = 40001;pkt.udp.destination = 40002;// set UDP payloadpkt.udp.SetData( 0, "Hello", 5 );// calculate UDP and IPv4 checksum and send Ethernet packetpkt.CompletePacket();output( pkt ); |
|---|

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 SP3 | 11.0 SP3 | 13.0 | — | 14 | 3.0 SP3 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | Ethernet | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |

| Version 15© Vector Informatik GmbH |
|---|
