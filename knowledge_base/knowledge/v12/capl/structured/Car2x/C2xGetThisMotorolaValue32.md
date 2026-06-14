# C2xGetThisMotorolaValue32

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetThisMotorolaValue32( long offset );
```

## Description

This function reads the data of a received packet in Motorola format.

## Return Values

Read value.

## Example

```c
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  dword value32;
  value32 = C2xGetThisMotorolaValue32( 0 );
}
```

## Availability

| Since Version |
|---|
