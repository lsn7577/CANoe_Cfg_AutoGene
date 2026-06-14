# C2xGetThisMotorolaValue16

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetThisMotorolaValue16( long offset );
```

## Description

This function reads the data of a received packet in Motorola format.

## Return Values

Read value.

## Example

```c
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  WORD value16;
  value16 = C2xGetThisMotorolaValue16( 0 );
}
```

## Availability

| Since Version |
|---|
