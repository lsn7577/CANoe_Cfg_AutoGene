# ethernetPacket Selectors: <protocol>.<optional-structure>.<field>

> Category: `IP` | Type: `notes`

## Description

byte ethernetPacket.<protocol>.<optional-structure>.<field>;

word ethernetPacket.<protocol>.<optional-structure>.<field>;

dword ethernetPacket.<protocol>.<optional-structure>.<field>;

qword ethernetPacket.<protocol>.<optional-structure>.<field>;

Read or write access to protocol-option fields within optional-structures.

See protocol overview for protocol and field designators.

If <protocol>, <optional-structure> or <field> is not contained in the packet, the measurement is stopped with a runtime error. ethernetPacket::<protocol>::<optional-structure>::IsAvailable can be used to find out if the field is available.

The data type depends on the protocol field. The bit length is rounded up to next larger CAPL data type, i.e. a 4-bit protocol field will use byte and a 12-bit protocol field will use word.

This selector is available for protocol field of type integer. For protocol fields, which are not integer values, the method GetData and SetData can be used.

—

| on key '1'{ ethernetPacket pkt; pkt.ipv6.Init();// initialize a packet IPv6 pkt.udp.Init(); // and UDP pkt.ipv6.fragment.Init(); pkt.ipv6.fragment.offset = 100; pkt.ipv6.framgent.flag = 1; pkt.ipv6.fragment.identification = 0x1234; pkt.CompletePacket(); output( pkt );} |
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
