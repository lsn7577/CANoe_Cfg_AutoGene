# C2xGetThisValue8

> Category: `Car2x` | Type: `function`

## Syntax

```c
C2xGetThisValue8( 14 );
```

## Description

This function reads the data of a received packet.

## Parameters

| Name | Description |
|---|---|
| offset | Byte offset relative to the beginning of a data packet or the payload (see description above). |

## Return Values

Read value.

## Example

```c
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  byte value8;
  value8 = C2xGetThisValue8( 14 );
  write( "Value %d", value8 );
}
```

## Availability

| Since Version |
|---|
