# EthGetThisValue32

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetThisValue32( long offset );
```

## Description

This function reads the data of a received packet in Intel format.

It is only usable in a CAPL callback function that had been registered with EthReceiveRawPacket or EthReceivePacket. It depends on the callback function, which part of the packet data is accessed by the function:

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  EthReceiveRawPacket( "OnEthRawPacket");
}
void OnEthRawPacket( LONG channel, LONG dir, LONG packetLength )
{
  BYTE rx_data[100];
  LONG rx_length:
  LONG val;

  // get the payload of the packet
  rx_length = EthGetThisData( 0, elCount(rx_data), rx_data );

  // get 32-bit integer value at offset 0 of the payload
  val = EthGetThisValue32( 0 );
}
```

## Availability

| Up to Version |
|---|
