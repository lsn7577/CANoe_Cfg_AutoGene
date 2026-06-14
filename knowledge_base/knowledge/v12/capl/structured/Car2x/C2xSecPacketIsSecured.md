# C2xSecPacketIsSecured

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecPacketIsSecured (long packetHandle);
```

## Description

Checks if the packet is secured by a security layer (Security Header or WAVE Security Services).

## Return Values

1: the packet is secured

## Example

```c
void OnC2xPacket (long channel, long dir, long radioChannel, long signalStrength, long sigQuality, long packet)
{
  byte hashedId8[8] ;

  if (C2xSecPacketIsSecured(packet))
  {
    C2xSecPacketGetSignerHashedId8(packet, hashedId8);
    /* ... */
  }
}
```

## Availability

| Since Version |
|---|
