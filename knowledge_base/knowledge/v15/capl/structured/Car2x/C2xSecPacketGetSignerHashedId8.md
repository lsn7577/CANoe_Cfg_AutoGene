# C2xSecPacketGetSignerHashedId8

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecPacketGetSignerHashedId8( long packetHandle, byte signerHashedId8[] );
```

## Description

Gets the HashedId8 digest of the certificate which was used to sign the packet.

## Parameters

| Name | Description |
|---|---|
| packetHandle | Handle of the packet. |
| signerHashedId8 | Buffer in which the digest is copied, size must be 8 byte. |

## Example

```c
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long rxPacketHandle )
{
  byte hashedId8[8];
  C2xSecPacketGetHashedId8(rxPacketHandle, hashedId8);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | — | — | — | 2.1 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
