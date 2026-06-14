# ethernetPacket::protocol::optional-structure::Clear

> Category: `IP` | Type: `method`

## Syntax

```c
long ethernetPacket.<protocol>.<optional-structure>.Clear();
```

## Description

Removes a protocol option from the Ethernet packet.

## Example

```c
on ethernetPacket msgChannel1.*
{
  if (this.ipv6.fragment.IsAvailable()
  {
    ethernetPacket pkt;

    // copy packet
    pkt            = this;
    pkt.msgChannel = 2;

    // remove option fragment
    pkt.ipv6.fragment.Clear();

    // recalculate checksums and output packet
    pkt.CompletePacket();
    output( pkt )
  }
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
