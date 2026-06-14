# ethStopPacketGenerator

> Category: `IP` | Type: `function`

## Syntax

```c
long ethStopPacketGenerator( ethernetPacket txPacket );
```

## Description

Stops the Ethernet packet generator, which was started with EthStartPacketGenerator.

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
  EthStartPacketGenerator( txPacket, 1000 );
}

on key '2'
{
  ethStopPacketGenerator(txPacket);
}
```

## Availability

| Since Version |
|---|
