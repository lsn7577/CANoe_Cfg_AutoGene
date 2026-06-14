# C2xSecPacketSetSignerHandle

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecPacketSetSignerHandle( long packetHandle, long certificateHandle );
```

## Description

Assigns a certificate to a Tx packet.

The assigned certificate is used to sign the Tx packet when C2xCompletePacket(packetHandle) is called.

The protocol type and version of the packet must match the protocol type and version of the certificate. E.g. an ETSI TS 103 097 encoded message cannot be signed using an IEEE 1609.2 encoded certificate.

## Return Values

0 or error code

## Example

```c
long packetHandle;
long certificateHandle;
packetHandle = C2xInitPacket("geo_eh", "BEACON | SH");
certificateHandle = C2xSecCertificateGetHandle ( "MyCert" );
C2xSecPacketSetSignerHandle(packetHandle, certificateHandle);
C2xCompletePacket(packetHandle);
C2xOutputPacket(packetHandle);
```

## Availability

| Since Version |
|---|
