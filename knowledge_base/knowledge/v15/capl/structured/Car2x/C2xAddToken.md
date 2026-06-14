# C2xAddToken

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xAddToken( long packet, char protocolDesignator[], char tokenDesignator[] );
```

## Description

This function adds an additional token at the end of a protocol header.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket |
| protocolDesignator | Name of the protocol |
| tokenDesignator | Name of the token |

## Example

```c
long packetHandle = 0;
packetHandle = C2xInitPacket("wsmp");
C2xAddToken(packetHandle, "wsmp", "transmitPower");
C2xAddToken(packetHandle, "wsmp", "dataRate");
C2xAddToken(packetHandle, "wsmp", "channelNumber");
C2xCompletePacket(packetHandle);
C2xOutputPacket(packetHandle);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 | — | — | — | 2.1 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
