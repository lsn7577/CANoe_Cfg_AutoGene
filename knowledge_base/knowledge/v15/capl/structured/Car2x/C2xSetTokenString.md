# C2xSetTokenString

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetTokenString( long packet, char protocolDesignator[], char tokenDesignator[], char data[] );
long C2xSetTokenString( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, char data[] );
```

## Description

This function copies the string value to the token without terminating \0.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket. |
| protocolDesignator | Name of the protocol, e.g. geo_cnh. |
| tokenDesignator | Name of the token, e.g. data. |
| byteOffset | Offset from the beginning of the token in byte. |
| data | Data as string. |

## Example

```c
long packetHandle;

// create packet
packetHandle = C2xInitPacket( "geo_cnh" );

// set geo_cnh payload
C2xResizeToken( packetHandle, "geo_cnh", "data", 5*8 /*bits*/ );
C2xSetTokenString( packetHandle, "geo_cnh", "data", "Hello" );

// complete and send packet
C2xCompletePacket( packetHandle );
C2xOutputPacket( packetHandle );

// release packet
C2xReleasePacket( packetHandle );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6: form 1, 2 | — | — | — | 2.1 SP3: form 1, 2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
