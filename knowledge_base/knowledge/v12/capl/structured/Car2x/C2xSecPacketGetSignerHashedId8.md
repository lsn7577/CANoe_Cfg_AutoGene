# C2xSecPacketGetSignerHashedId8

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecPacketGetSignerHashedId8( long packetHandle, byte signerHashedId8[] );
```

## Description

Gets the HashedId8 digest of the certificate which was used to sign the packet.

## Return Values

Number of bytes copied

## Example

```c
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long rxPacketHandle )
{
  byte hashedId8[8];
  C2xSecPacketGetHashedId8(rxPacketHandle, hashedId8);
}
```

## Availability

| Since Version |
|---|
