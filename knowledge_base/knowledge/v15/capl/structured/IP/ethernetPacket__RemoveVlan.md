# ethernetPacket::RemoveVlan

> Category: `IP` | Type: `method`

## Syntax

```c
long ethernetPacket.RemoveVlan(); // form 1
long ethernetPacket.RemoveVlan(dword vlanIndex); // form 2
```

## Description

Removes a VLAN tag from an Ethernet packet.

To remove a specific VLAN tag from a double-tagged packet form 2 can be used.

## Parameters

| Name | Description |
|---|---|
| vlanIndex | Index of the VLAN tag for double-tagged VLANs. Index 0 is the inner VLAN, index 1 the outer VLAN.Range 0..2 |

## Example

```c
on ethernetPacket *
{
  if ((this.hasVlan()) && (this.msgChannel == 1))
  {
    ethernetPacket forwardPkt;

    forwardPkt = this;
    forwardPkt.msgChannel = 2;
    forwardPkt.RemoveVlan();

    output( forwardPkt );
  }
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
