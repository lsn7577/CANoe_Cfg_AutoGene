# C2xGetThisValue16

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetThisValue16( long offset );
```

## Description

This function reads the data of a received packet in Intel format.

## Return Values

Read value.

## Example

```c
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  word value16;
  value16 = C2xGetThisValue16( 14 );
  write( "Value %d", value16 );
}
```

## Availability

| Since Version |
|---|
