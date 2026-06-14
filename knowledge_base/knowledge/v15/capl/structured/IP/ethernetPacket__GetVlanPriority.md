# ethernetPacket::GetVlanPriority

> Category: `IP` | Type: `method`

## Syntax

```c
dword ethernetPacket.GetVlanPriority(); // form 1
dword ethernetPacket.GetVlanPriority(dword vlanIndex); // form 2
```

## Description

Returns the VLAN priority, if the Ethernet packet contains a VLAN tag.For double-tagged VLAN form 2 can be used to access a specific VLAN priority.

## Parameters

| Name | Description |
|---|---|
| vlanIndex | Index of the VLAN tag for double-tagged VLANs. Index 0 is the inner VLAN, index 1 the outer VLAN.Range: 0..2 |

## Return Values

ID of the VLAN or 0xFFFF if no VLAN is available.

## Example

```c
on ethernetPacket *
{
  if (this.hasVlan())
  {
    word vlanPrio;

    vlanPrio = this.GetVlanPriority();

    write( "Received Ethernet packet with VLAN priority %d", vlanPrio );
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
