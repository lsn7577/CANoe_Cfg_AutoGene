# ethernetPacket::SetVlanId

> Category: `IP` | Type: `method`

## Syntax

```c
long ethernetPacket.SetVlanId(word vlanId); // form 1
long ethernetPacket.SetVlanId(dword vlanIndex, word vlanId); // form 2
```

## Description

Sets the VLAN ID of an Ethernet packet. If the packets does not contain a VLAN tag, a new VLAN tag is added.

For double-tagged VLAN form 2 can be used.

## Parameters

| Name | Description |
|---|---|
| vlanId | The VLAN ID to set.Range: 0..0FFFh |
| vlanIndex | Index of the VLAN tag for double-tagged VLANs. Index 0 is the inner VLAN, index 1 the outer VLAN.Range 0..2 |

## Example

```c
on key '1'
{
  ethernetPacket pkt;

  pkt.SetVlanId( 10 );
  pkt.SetVlanPriority( 1 );

  output( pkt );
}

on key '2'
{
  ethernetPacket pkt;

  // double tagged VLAN
  pkt.SetVlanId( 0, 10 );
  pkt.SetVlanPriority( 0, 1 );
  pkt.SetVlanId( 1, 20 );
  pkt.SetVlanPriority( 1, 2 );

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
