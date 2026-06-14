# EthIsPacketValid

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthIsPacketValid( long packet );
```

## Description

The function checks, if a received packet has a protocol error. Packets with a protocol error are marked with an error icon in the Trace Window.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  EthReceivePacket( "OnEthPacket");
}
void OnEthPacket( LONG channel, LONG dir, LONG packet )
{
  if (EthIsPacketValid( packet ) != 0)
  {
    write( "Receive packet with protocol error" );
  }
}
```

## Availability

| Up to Version |
|---|
