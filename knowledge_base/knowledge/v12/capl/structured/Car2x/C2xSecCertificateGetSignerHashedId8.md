# C2xSecCertificateGetSignerHashedId8

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateGetSignerHashedId8( long certificateHandle, byte signerHashedId8[] );
```

## Description

Gets the signer (parent) certificate’s HashedId8 digest. In some protocols the digest is called CertId8.

## Return Values

number of bytes copied

## Example

```c
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long rxPacketHandle )
{
  long certificateHandle;
  byte signerHashedId8[8];
  certificateHandle = C2xSecPacketGetSignerHandle( rxPacketHandle );
  if (certificateHandle != 0)
  {
  C2xSecCertificateGetSignerHashedId8(certificateHandle, signerHashedId8);
  }
}
```

## Availability

| Since Version |
|---|
