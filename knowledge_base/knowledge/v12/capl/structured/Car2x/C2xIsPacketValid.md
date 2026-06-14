# C2xIsPacketValid

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xIsPacketValid( long packet );
```

## Description

This function checks, if a received packet has a protocol error. Packets with a protocol error are marked with an error icon in the Trace Window.

## Return Values

0: packet is valid

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  C2xReceivePacket( "OnC2xPacket");
}
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  if (C2xIsPacketValid( packet ) != 0)
  {
    write( "Receive packet with protocol error" );
  }
}
```

## Availability

| Since Version |
|---|
