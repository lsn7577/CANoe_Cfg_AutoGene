# ethernetPacket::SetVlan

> Category: `IP` | Type: `method`

## Syntax

```c
long ethernetPacket.SetVlan(word tpid,word tci); // form 1
long ethernetPacket.SetVlan(dword vlanIndex, word tpid,word tci); // form 2
```

## Description

Sets the VLAN tag of an Ethernet packet. If the packets does not contain a VLAN tag, a new VLAN tag is added.

For double-tagged VLAN form 2 can be used.

## Parameters

| Name | Description |
|---|---|
| tpid | VLAN TPDI value to set. |
| tci | VLAN TCI value to set |
| vlanIndex | Index of the VLAN tag for double-tagged VLANs. Index 0 is the inner VLAN, index 1 the outer VLAN.Range: 0..2 |

## Example

```c
on key '1'
{
  ethernetPacket pkt;

  pkt.SetVlan( 0x8100, 0x5123 );

  output( pkt );
}

on key '2'
{
  ethernetPacket pkt;

  // double tagged VLAN
  pkt.SetVlan( 0, 0x8100, 0x5123 );
  pkt.SetVlan( 1, 0x88A8, 0x6456 );

  output( pkt );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | — | — | 2.2 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
