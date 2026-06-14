# C2xSecPacketGetStatus

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecPacketGetStatus( long packetHandle );
```

## Description

Gets validity status of a packet.

This is interesting for received packets only and indicates, if the signature of the security header of the packet is valid. In case the signature is not valid, an appropriate error code is returned.

## Parameters

| Name | Description |
|---|---|
| packetHandle | Handle of the packet. |

## Return Values

The validity status consists of 3 bit fields which are combined using a binary OR operation.
The overall status is masked with 0xf000 and has the meaning:
The relevant subject in the trust chain is identified by the mask 0x0f00:
In case of an invalid status the reason is specified by the mask 0x000f:
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
