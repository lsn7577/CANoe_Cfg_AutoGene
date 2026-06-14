# ethernetPacket::source::ParseAddress

> Category: `IP` | Type: `method`

## Syntax

```c
long ethernetPacket.source.ParseAddress( char addressAsString[] ); // form 1
long ethernetPacket.destination.ParseAddress( char addressAsString[] ); // form 2
```

## Description

Sets the source or destination MAC address of an Ethernet packet with a string.

The address must be given in this form: 02:00:00:12:34:AB

## Parameters

| Name | Description |
|---|---|
| addressAsString | Address in text form of format MAC address. |

## Example

```c
ethernetPacket pkt;

pkt.source.ParseAddress( "02:00:00:00:00:01" );
pkt.destination.ParseAddress( "FF:FF:FF:FF:FF:FF" );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
