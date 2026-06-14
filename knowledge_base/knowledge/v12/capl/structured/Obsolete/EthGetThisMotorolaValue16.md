# EthGetThisMotorolaValue16

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetThisMotorolaValue16( long offset );
```

## Description

This function reads the data of a received packet in Motorola format.

It is only usable in a CAPL callback function that had been registered with EthReceiveRawPacket or EthReceivePacket. It depends on the callback function, which part of the packet data is accessed by the function:

## Example

```c
void OnEthRawPacket( LONG channel, LONG dir, LONG packetLength )
{
  switch(EthGetThisMotorolaValue16( 12 ))
  {
  case 0x800: write( "IPv4" ); break;
  case 0x806: write( "ARP" ); break;
  }
}
```

## Availability

| Up to Version |
|---|
