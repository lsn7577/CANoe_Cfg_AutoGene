# C2xGetThisData

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetThisData( long offset, long bufferSize, byte buffer[] );
```

## Description

This function gets the payload data of the highest interpretable protocol.

## Return Values

Number of copied data bytes.

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
  byte payload[8];
  long len;

  len = C2xGetThisData( 0, 8, payload);
  write( "Receive payload with %d bytes", len );
}
```

## Availability

| Since Version |
|---|
