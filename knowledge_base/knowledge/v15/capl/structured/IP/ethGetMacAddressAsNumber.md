# ethGetMacAddressAsNumber

> Category: `IP` | Type: `function`

## Syntax

```c
qword ethGetMacAddressAsNumber( char macAddrStr[] );
```

## Description

Converts a MAC address string, i.e. "02:00:00:00:00:01", to a qword-number, which can be used with ethernetPacket.source and ethernetPacket.destination.

## Parameters

| Name | Description |
|---|---|
| macAddrStr | MAC address as string, i.e. "02:00:00:00:00:01". |

## Return Values

The MAC address as qword or 0, if failed

## Example

```c
on key '1'
{
  ethernetPacket txPacket;
  txPacket.msgChannel = 1;
  txPacket.source      = ethGetMacAddressAsNumber( "20:00:00:00:00:01" );
  txPacket.destination = ethGetMacAddressAsNumber( "FF:FF:FF:FF:FF:FF" );
  txPacket.Length      = 100;
  txPacket.type        = 0xF123;
  output( txPacket );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | 13.0 | 13.0 | — | 2.0 SP2 |
| Restricted To | Ethernet | Ethernet | Ethernet | Ethernet | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
