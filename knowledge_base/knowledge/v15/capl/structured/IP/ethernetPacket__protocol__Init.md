# ethernetPacket::protocol::Init

> Category: `IP` | Type: `method`

## Syntax

```c
long ethernetPacket.<protocol>.Init();
```

## Description

Initialize the protocol within an Ethernet packet. It appends the protocol, if it is not already contained in the packet and initialized the protocol header with default values. If a protocol requires other underlaying protocols, it will add these protocols too, i.e. if the UDP protocol is initialized it also adds an IPv4 protocol header by default. If a specific protocol stack is required, the Init() function can be called for every protocol from the lower protocols to the upper protocols, i.e. if UDP over IPv6 is required, first initialize IPv6 and then UDP. Higher protocols than the one which is initialized, will be removed.

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
