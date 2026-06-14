# C2xGetThisValue64

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetThisValue64( long offset );
```

## Description

This function reads the data of a received packet in Intel format.

## Return Values

Read value.

## Example

```c
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  qword value64;
  value64 = C2xGetThisValue64( 14 );
  write( "Value %I64d", value64 );
}
```

## Availability

| Since Version |
|---|
