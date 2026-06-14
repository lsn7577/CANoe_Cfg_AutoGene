# ethernetPacket::protocol::optional-structure::Init

> Category: `IP` | Type: `method`

## Syntax

```c
long ethernetPacket.<protocol>.<optional-structure>.Init();
```

## Description

Add a protocol option for a specific protocol to the Ethernet packet. The protocol must support options. Following options are available:

## Return Values

0 – Success
-1 – Error

## Example

```c
on key '1'
{
  ethernetPacket pkt;
  pkt.ipv6.Init();// initialize a packet IPv6
  pkt.udp.Init(); // and UDP
  pkt.ipv6.fragment.Init();
  pkt.ipv6.fragment.offset = 100;
  pkt.ipv6.framgent.flag  = 1;
  pkt.ipv6.fragment.identification = 0x1234;
  pkt.CompletePacket();
  output( pkt );
}
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
