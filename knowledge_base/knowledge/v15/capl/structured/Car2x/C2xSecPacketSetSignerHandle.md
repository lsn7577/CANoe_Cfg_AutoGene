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

## Parameters

| Name | Description |
|---|---|
| packetHandle | Handle of the packet. |
| certificateHandle | Handle of the certificate. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
