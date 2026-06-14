# C2xSecCertificateGetHashedId8

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateGetHashedId8( long certificateHandle, byte hashedId8[] );
```

## Description

Gets HashedId8 digest of a certificate.

## Return Values

number of bytes copied

## Example

```c
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long rxPacketHandle )
{
  long certificateHandle;
  byte hashedId8[8];
  certificateHandle = C2xSecPacketGetSignerHandle(rxPacketHandle);
  C2xSecCertificateGetHashedId8(certificateHandle, hashedId8);
}
```

## Availability

| Since Version |
|---|
