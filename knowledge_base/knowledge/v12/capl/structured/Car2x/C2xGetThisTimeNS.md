# C2xGetThisTimeNS

> Category: `Car2x` | Type: `function`

## Syntax

```c
qword C2xGetThisTimeNS( void );
```

## Description

This function returns the time stamp of an received WLAN packet in nanoseconds.

## Return Values

Time stamp in nanoseconds

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  C2xReceivePacket("OnC2xPacket");
}
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  float t;
  t = (float)C2xGetThisTimeNS();
  write("Received packet at %f [ns]", t );
}
```

## Availability

| Since Version |
|---|
