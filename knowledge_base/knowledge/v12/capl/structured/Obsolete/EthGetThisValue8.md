# EthGetThisValue8

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetThisValue8( long offset );
```

## Description

This function reads the data of a received packet.

It is only usable in a CAPL callback function that had been registered with EthReceiveRawPacket or EthReceivePacket. It depends on the callback function, which part of the packet data is accessed by the function:

## Example

```c
void OnEthRawPacket( LONG channel, LONG dir, LONG packetLength )
  
{

  BYTE value;

  value = EthGetThisValue8( 14 );


     write( "Value %d", value );
  
}
```

## Availability

| Up to Version |
|---|
