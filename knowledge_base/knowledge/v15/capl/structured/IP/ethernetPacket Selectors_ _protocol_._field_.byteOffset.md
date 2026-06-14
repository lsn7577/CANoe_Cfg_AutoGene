# ethernetPacket Selectors: <protocol>.<field>.byteOffset

> Category: `IP` | Type: `notes`

## Description

dword ethernetPacket.<protocol>.<field>.byteOffset;

Byte offset of a protocol field. The selector is read only.

Offset 0 is directly after the Ethertype.

If <protocol> or <field> is not contained in the packet, the selector returns 0. ethernetPacket::protocol::field::IsAvailable can be used to find out if the field is available.

—

| ethernetPacket pkt;word offset, length;// initialize packet with IPv4 and UDP protocolspkt.udp.Init();pkt.udp.ResizeData(10);offset = pkt.udp.checksum.byteOffset;length = pkt.udp.checksum.byteLength;write( "Protocol field udp.checksum is at byte %d:%d", offset, length ); |
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
