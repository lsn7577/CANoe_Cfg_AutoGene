# C2xSecPacketIsSecured

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecPacketIsSecured (long packetHandle);
```

## Description

Checks if the packet is secured by a security layer (Security Header or WAVE Security Services).

## Parameters

| Name | Description |
|---|---|
| packetHandle | Handle of the packet. |

## Example

```c
void OnC2xPacket (long channel, long dir, long radioChannel, long signalStrength, long sigQuality, long packet)
{
  byte hashedId8[8] ;

  if (C2xSecPacketIsSecured(packet))
  {
    C2xSecPacketGetSignerHashedId8(packet, hashedId8);
    /* ... */
  }
}
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
