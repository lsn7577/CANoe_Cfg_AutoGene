# ethStartPacketGenerator

> Category: `IP` | Type: `function`

## Syntax

```c
long ethStartPacketGenerator( ethernetPacket txPacket, dword transmissionRate );
```

## Description

Starts the Ethernet packet generator that sends continuously the configured packets.

It is possible to run the packet generator for one packet per Ethernet channel. If you do not specify a number of Frames the generator sends until you call EthStopPacketGenerator.

## Return Values

0: Success

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

| Since Version |
|---|
