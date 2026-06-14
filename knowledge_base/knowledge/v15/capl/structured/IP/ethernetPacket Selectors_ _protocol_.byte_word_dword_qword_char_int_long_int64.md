# ethernetPacket Selectors: <protocol>.byte/word/dword/qword/char/int/long/int64

> Category: `IP` | Type: `notes`

## Description

byte ethernetPacket.<protocol>.Byte ( index );

word ethernetPacket.<protocol>.Word ( index );

dword ethernetPacket.<protocol>.DWord( index );

qword ethernetPacket.<protocol>.QWord( index );

char ethernetPacket.<protocol>.Char ( index );

int ethernetPacket.<protocol>.Int ( index );

long ethernetPacket.<protocol>.Long ( index );

int64 ethernetPacket.<protocol>.Int64 ( index );

Access to the payload of a protocol.

If index is greater than available data or <protocol> is not contained in the packet, the measurement is stopped with a runtime error. ethernetPacket::protocol::IsAvailable and ethernetPacket::protocol::byteLength can be used to find out if the data is available.

Byte offset. Index 0 is the first byte within the payload of the protocol. If index is greater than ethernetPacket.<protocol>.byteLength a runtime error occurs.

Value at specified index.

| Index | Byte offset. Index 0 is the first byte within the payload of the protocol. If index is greater than ethernetPacket.<protocol>.byteLength a runtime error occurs. |
|---|---|

| on ethernetPacket *{ if ((this.udp.IsAvailable()) && (this.udp.byteLength >= 16)) { word val; val = this.udp.Word(15); }}on key '1'{ int i; ethernetPacket pkt; // initialize packet with IPv4 and UDP protocols pkt.udp.Init(); // set IPv4 addresses pkt.ipv4.source.ParseAddress( "192.168.1.1" ); pkt.ipv4.destination.ParseAddress( "192.168.1.255" ); // set UDP ports pkt.udp.source = 40001; pkt.udp.destination = 40002; // set UDP payload pkt.udp.ResizeData( 10 ); for( i = 0; i < 10; i++ ) { pkt.udp.Byte(i) = i; } // calculate UDP and IPv4 checksum and send Ethernet packet pkt.CompletePacket(); output( pkt );} |
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
