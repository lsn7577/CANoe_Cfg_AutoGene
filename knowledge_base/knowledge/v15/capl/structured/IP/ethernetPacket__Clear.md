# ethernetPacket::Clear

> Category: `IP` | Type: `method`

## Syntax

```c
void ethernetPacket.Clear();
```

## Description

Clears data and resets length.

## Return Values

—

## Example

```c
ethernetPacket pkt;

// prepare packet for first output
pkt.ipv6.Init();
pkt.udp.Init();
pkt.udp.SetData( 0, "Hello", 5 );
pkt.CompletePacket();
output( pkt );

// clear the packet
pkt.Clear();

// prepare packet for second output with different
// protocols and data than with first output above

pkt.tcp.Init();
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
