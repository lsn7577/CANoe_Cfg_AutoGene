# EthGetThisData

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetThisData( long offset, long bufferSize, byte buffer[] );
```

## Description

The function gets the returned data.

It is only usable in a CAPL callback function that had been registered with EthReceiveRawPacket or EthReceivePacket. It depends on the callback function, which part of the packet data is accessed by the function:

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  EthReceiveRawPacket( "OnEthRawPacket");
}
void OnEthRawPacket( LONG channel, LONG dir, LONG packetLength)
{
  BYTE dstMac[6];

  if (EthGetThisData( 0, 6, dstMac) == 6)
  {
    write( "Destination %.2x:%.2x:%.2x:%.2x:%.2x:%.2x", dstMac[0], dstMac[1], dstMac[2], dstMac[3], dstMac[4], dstMac[5] );
  }
}
```

## Availability

| Up to Version |
|---|
