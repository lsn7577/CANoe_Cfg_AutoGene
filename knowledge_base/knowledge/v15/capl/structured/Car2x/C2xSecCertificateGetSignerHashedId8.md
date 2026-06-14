# C2xSecCertificateGetSignerHashedId8

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateGetSignerHashedId8( long certificateHandle, byte signerHashedId8[] );
```

## Description

Gets the signer (parent) certificate’s HashedId8 digest. In some protocols the digest is called CertId8.

## Parameters

| Name | Description |
|---|---|
| certificateHandle | Handle of the certificate. |
| signerHashedId8 | Buffer in which the digest is copied, size must be 8 byte. |

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
