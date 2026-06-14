# ethStartPacketGenerator

> Category: `IP` | Type: `function`

## Syntax

```c
long ethStartPacketGenerator( ethernetPacket txPacket, dword transmissionRate );
long ethStartPacketGenerator( ethernetPacket txPacket, dword transmissionRate, dword numberOfFrames );
long ethStartPacketGenerator( ethernetPacket txPacket, dword transmissionRate, dword numberOfFrames, dword counterByteOffset );
```

## Description

Starts the Ethernet packet generator that sends continuously the configured packets.

It is possible to run the packet generator for one packet per Ethernet channel or port. If you do not specify a number of Frames the generator sends until you call EthStopPacketGenerator.

## Parameters

| Name | Description |
|---|---|
| txPacket | The Ethernet packet to send. |
| transmissionRate | The rate in frames per second the packet should be transmitted. Range: [1 ... 1.000.000] in channel-based mode. Range: [1 ... 30.000.000] in network-based mode. |
| numberOfFrames | The number of Frames that should be transmitted overall. Range: [0x1 ... 0xFFFFFFFE], 0xFFFFFFFF to send until EthStopPacketGenerator. |
| counterByteOffset | The position a 4 byte counter is placed inside the Ethernet-payload on a zero based index. Index 0 is the first byte after the source MAC Address. Take care that the counter has to fit completely into the payload. E.g. for a packet with 100 byte Ethernet payload the highest position for a 4 byte counter is 96. |

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
  ethStartPacketGenerator( txPacket, 1000 );
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
