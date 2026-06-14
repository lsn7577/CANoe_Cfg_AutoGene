# ethInjectPacket

> Category: `IP` | Type: `function`

## Syntax

```c
long ethInjectPacket (ethernetPacket packet, byte direction);
```

## Description

Transmits an Ethernet packet by a specific ethernetPort defined in <packet>. Allows to output a frame not only on a simulation port like output, but on a physical port as well e.g. for error injection.

## Parameters

| Name | Description |
|---|---|
| packet | Variable of type ethernetPacket. |
| direction | transmit direction from viewpoint of the connected segment: <rx> or <0> to send from a simulated port (into the connected segment) in real mode <tx> or <1> to send from a physical measurement port (away from the connected segment) in real mode in simulated mode use <tx> or <rx> (respectively <0> or <1>) to send from simulated ports either into the connected segment (rx) or away from the connected segment (tx). |

## Example

```c
ethernetPacket txPacket;

txPacket.hwPort = lookupEthernetPort(„Ethernet1::Port1“);
txPacket.source = EthGetMacAddressAsNumber( "20:00:00:00:00:01" );
txPacket.destination = EthGetMacAddressAsNumber( "FF:FF:FF:FF:FF:FF" );
txPacket.Length = 100;
txPacket.type = 0xF123;

ethInjectPacket( txPacket, tx );  // send over physical port <Port1> of network <Ethernet1>
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 SP5 | 12.0 SP5 | 13.0 | — | — | 5.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
