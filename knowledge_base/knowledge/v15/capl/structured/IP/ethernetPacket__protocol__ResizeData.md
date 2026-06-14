# ethernetPacket::protocol::ResizeData

> Category: `IP` | Type: `method`

## Syntax

```c
long ethernetPacket.<protocol>.ResizeData( word newLength );
```

## Description

Resizes the payload of a protocol within an Ethernet packet.

If the newLength is greater than the length of the Ethernet packet, the Ethernet packet is enlarged.

If <protocol> is not available in the packet, an error is returned.

## Parameters

| Name | Description |
|---|---|
| newLength | New length in bytes |

## Example

```c
word i;
ethernetPacket pkt;

pkt.udp.Init();
pkt.udp.ResizeData( 200 );

for (i = 0; i < 200; i++ )
{
  pkt.udp.Byte(i) = 0;
}

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
