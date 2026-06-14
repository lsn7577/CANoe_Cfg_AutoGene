# C2xSecPacketGetStatus

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecPacketGetStatus( long packetHandle );
```

## Description

Gets validity status of a packet.

This is interesting for received packets only and indicates, if the signature of the security header of the packet is valid. In case the signature is not valid, an appropriate error code is returned.

## Return Values

The validity status consists of 3 bit fields which are combined using a binary OR operation
Status examples:

## Example

```c
variables
{
  byte hashedId8[8];
}

void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long rxPacketHandle )
{
  long rxCertificateHandle;
  switch (C2xSecPacketGetStatus(rxPacketHandle) & 0xF000)
  {
    case 0x0000: break; // no SH included or other error
    case 0x1000:            // unknown
    {
      // get the certificate digest
      C2xGetTokenData(rxPacketHandle, "geo_sh", "signerHashedId", elCount(hashedId8), hashedId8);
      break;
    }
    case 0x2000: // invalid
    {
      // check used certificate
      break;
    }
    case 0x3000: break; // valid
  }
}
```

## Availability

| Since Version |
|---|
