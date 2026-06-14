# AfdxSetTokenString

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetTokenString( long packet, long protocolDesignator[], long tokenDesignator[], long offset, char data[] );
```

## Description

This function copies the string value to the token without terminating "\0".

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket. |
| protocolDesignator | Name of the protocol, e.g. "afdx". |
| tokenDesignator | Name of the token, e.g. "data". |
| offset | This is the offset from the beginning of the token's data area. If this is 0, data is copied starting at byte 0 of the token's data area. |
| data | Data as string. |

## Example

```c
long packetHandle;

// create packet
packetHandle = AfdxInitPacket( "afdx" );

// set afdx payload
AfdxResizeToken( packetHandle, "afdx", "data", 5*8 /*bits*/ );
AfdxSetTokenString( packetHandle, "afdx", "data", "Hello" );

// Complete and send packet
AfdxCompletePacket( packetHandle );
AfdxOutputPacket( packetHandle );

// release packet
AfdxReleasePacket( packetHandle );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
