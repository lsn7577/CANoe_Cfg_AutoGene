# output (Ethernet)

> Category: `IP` | Type: `function`

## Syntax

```c
void output(ethernetPacket packet); // form 1
void output(ethernetPacket packet, dword fcs); // form 2
void output(ethernetErrorPacket packet); // form 3
```

## Description

Outputs an Ethernet packet (form 1) from the program block.Form 2 can be used to output Ethernet packets with an invalid frame checksum.

## Parameters

| Name | Description |
|---|---|
| packet | Variable of type ethernetPacket (form 1 and 2) or ethernetErrorPacket (form 3). |
| fcs | Ethernet frame check sequence. |

## Return Values

—

## Example

```c
ethernetPacket txPacket;

txPacket.msgChannel = 1;
txPacket.source      = EthGetMacAddressAsNumber( "20:00:00:00:00:01" );
txPacket.destination = EthGetMacAddressAsNumber( "FF:FF:FF:FF:FF:FF" );
txPacket.Length = 100;
txPacket.type = 0xF123;

output( txPacket, 0x1234 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | 13.0: form 1 | — | 2.0 SP2 |
| Restricted To | Ethernet | Ethernet | Ethernet | Ethernet | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
