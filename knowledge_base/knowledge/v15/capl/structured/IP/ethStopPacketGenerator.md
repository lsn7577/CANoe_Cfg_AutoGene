# ethStopPacketGenerator

> Category: `IP` | Type: `function`

## Syntax

```c
long ethStopPacketGenerator( ethernetPacket txPacket );
```

## Description

Stops the Ethernet packet generator, which was started with EthStartPacketGenerator.

## Parameters

| Name | Description |
|---|---|
| txPacket | The Ethernet packet which was used to start the generator. |

## Example

```c
variables
{
  ethernetPacket txPacket;
}

on key '1'
{
  txPacket.msgChannel  = 1;
  txPacket.source      = EthGetMacAddressAsNumber( "20:00:00:00:00:01" );
  txPacket.destination = EthGetMacAddressAsNumber( "FF:FF:FF:FF:FF:FF" );
  txPacket.Length      = 100;
  txPacket.type        = 0xF123;
  EthStartPacketGenerator( txPacket, 1000 );
}

on key '2'
{
  ethStopPacketGenerator(txPacket);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | — | — | — | 2.0 SP2 |
| Restricted To | Ethernet | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
