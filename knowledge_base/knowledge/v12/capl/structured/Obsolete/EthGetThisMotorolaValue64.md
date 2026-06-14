# EthGetThisMotorolaValue64

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetThisMotorolaValue64( long offset );
```

## Description

This function reads the data of a received packet in Motorola format.

It is only usable in a CAPL callback function that had been registered with EthReceiveRawPacket or EthReceivePacket. It depends on the callback function, which part of the packet data is accessed by the function:

## Example

```c
void OnEthRawPacket( LONG channel, LONG dir, LONG packetLength )
{

  switch(EthGetThisMotorolaValue64( 14 ))
  {

  case 1:
        write( "Value 1" );
        break;

  case 2:
        write( "Value 2" );
        break;
  }
}
```

## Availability

| Up to Version |
|---|
