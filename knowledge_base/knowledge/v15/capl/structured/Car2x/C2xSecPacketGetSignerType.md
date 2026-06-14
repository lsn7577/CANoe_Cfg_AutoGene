# C2xSecPacketGetSignerType

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecPacketGetSignerType(long packetHandle);
```

## Description

Retrieves how the message signer information is included in the message. The information can be transmitted as digest (HashedId8), certificate or certificate chain.

## Parameters

| Name | Description |
|---|---|
| packetHandle | Handle of the signed packet. |

## Example

```c
switch (C2xSecPacketGetSignerType(packetHandle))
{
case 0: // unsecured
  // ...
  break;
case 1: // digest
  // ...
  break;
case 2: // certificate
  // ...
  break;
case 3: // certificate chain
  // ...
  break;
default: // error
  // ...
  break;
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
