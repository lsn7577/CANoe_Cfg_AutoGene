# ethGetMacAddressAsString

> Category: `IP` | Type: `function`

## Syntax

```c
long ethGetMacAddressAsString( qword macAddr, char buffer[], dword bufferLength );
```

## Description

Converts a MAC address from qword to string. The function is helpful with ethernetPacket.source and ethernetPacket.destination.

## Parameters

| Name | Description |
|---|---|
| macAddr | MAC address as qword, i.e. from ethernetPacket.source. |
| buffer | Buffer where the MAC address string is copied to. |
| bufferLength | Length of buffer |

## Example

```c
on ethernetPacket *
{
  char macAddrStr[18];
  if (ethGetMacAddressAsString( this.source, macAddrStr, elcount(macAddrStr) ) == 0)
  {
    write("Received Ethernet packet from %s", macAddrStr );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | 13.0 | — | — | 2.0 SP2 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
