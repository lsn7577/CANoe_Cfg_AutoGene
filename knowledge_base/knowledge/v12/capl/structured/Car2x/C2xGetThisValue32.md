# C2xGetThisValue32

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetThisValue32( long offset );
```

## Description

This function reads the data of a received packet in Intel format.

## Return Values

Read value.

## Example

```c
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  byte rx_data[100];
  long rx_length:
  long val32;

  // get the payload of the packet
  rx_length = C2xGetThisData( 0, elCount(rx_data), rx_data );

  // get 32-bit integer value at offset 0 of the payload
  val32 = C2xGetThisValue32( 0 );
}
```

## Availability

| Since Version |
|---|
