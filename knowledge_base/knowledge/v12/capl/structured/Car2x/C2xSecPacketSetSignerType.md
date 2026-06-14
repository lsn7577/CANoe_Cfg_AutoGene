# C2xSecPacketSetSignerType

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecPacketSetSignerType(long packetHandle, long signerType);
```

## Description

Specifies how the message signer information is included in the message. It is possible to add only a digest (HashedId8), to transmit the signer’s certificate or to transmit the complete certificate chain.

## Return Values

0 or error code

## Example

```c
long packetHandle;
long certificateHandle;
packetHandle = C2xInitPacket("geo_eh", "BEACON | SH");
certificateHandle = C2xSecCertificateGetHandle ( "MyCert" );
C2xSecPacketSetSignerHandle(packetHandle, certificateHandle);
C2xSecPacketSetSignerType(packetHandle, 2); // send certificate
C2xCompletePacket(packetHandle);
C2xOutputPacket(packetHandle);
```

## Availability

| Since Version |
|---|
