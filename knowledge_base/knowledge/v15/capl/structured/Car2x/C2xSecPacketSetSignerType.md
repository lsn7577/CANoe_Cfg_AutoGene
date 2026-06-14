# C2xSecPacketSetSignerType

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecPacketSetSignerType(long packetHandle, long signerType);
```

## Description

Specifies how the message signer information is included in the message. It is possible to add only a digest (HashedId8), to transmit the signer’s certificate or to transmit the complete certificate chain.

## Parameters

| Name | Description |
|---|---|
| packetHandle | Handle of the packet |
| signerType | Signer information type 0: unsecured 1: digest 2: certificate 3: certificate chain |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | — | — | — | 2.2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
