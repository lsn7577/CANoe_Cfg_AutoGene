# ethernetPacket Selectors: <protocol>.byteLength

> Category: `IP` | Type: `notes`

## Description

dword ethernetPacket.<protocol>.byteLength;

Returns the length of the payload of the protocol. The selector is read only.

If <protocol> is not contained in the packet, the selector returns 0. ethernetPacket::protocol::IsAvailable can be used to find out if the protocol is available.

—

Length of the protocol payload in bytes.

| ethernetPacket pkt;word offset, length, i;// initialize packet with IPv4 and UDP protocolspkt.udp.Init();pkt.udp.ResizeData(10);offset = pkt.udp.byteOffset;length = pkt.udp.byteLength;write( "Protocol udp is at byte %d:%d", offset, length );for( i = 0; i < length; i++ ){ pkt.byte( offset+i ) = i;}// calculate UDP and IPv4 checksum and send Ethernet packetpkt.CompletePacket();output( pkt ); |
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
