# <OnC2xPacket>

> Category: `Car2x` | Type: `function`

## Syntax

```c
void <OnC2xPacket>( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet );
```

## Description

This callback is called when a registered WLAN packet is received.

Within this callback the following functions can be used to retrieve the received packet data:

This functions access the payload of the highest interpretable protocol. Offset 0 starts at the beginning of the payload.

## Return Values

—

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  C2xReceivePacket( "OnC2xPacket");
}
void <OnC2xPacket>( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  byte rx_data[100];
  long rx_length;
  // get the payload of the packet
  rx_length = C2xGetThisData( 0, elCount(rx_data), rx_data );
  // do something with rx_data
}
```

## Availability

| Since Version |
|---|
