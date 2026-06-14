# C2xGetThisMotorolaValue64

> Category: `Car2x` | Type: `function`

## Syntax

```c
C2xGetThisMotorolaValue64( 0 );
```

## Description

This function reads the data of a received packet in Motorola format.

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
  QWORD value64;
  value64 = C2xGetThisMotorolaValue64( 0 );
}
```

## Availability

| Since Version |
|---|
