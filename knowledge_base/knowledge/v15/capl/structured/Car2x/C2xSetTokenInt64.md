# C2xSetTokenInt64

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetTokenInt64( long packet, char protocolDesignatorl[], char tokenDesignator[], int64 value ); // form 1
long C2xSetTokenInt64( long packet, char protocolDesignatorl[], char tokenDesignator[], long byteOffset, int64 length, long networkByteOrder, int64value ); // form 2
```

## Description

This function sets the integer value of a token.

Form 2 with byte offset sets a part of the token data as integer.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket. |
| protocolDesignator | Name of the protocol, e.g. geo_cnh. |
| tokenDesignator | Name of the token, e.g. lpvSpeed. |
| byteOffset | Offset from the beginning of the token in byte. |
| length | Length of the integer value, up to 8 byte. |
| networkByteOrder | 0: INTEL (little-endian) 1: MOTOROLA (big-endian) |
| value | New integer value. |

## Example

See example of C2xInitPacket.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 SP3: form 1, 2 | — | — | — | 2.1 SP3: form 1, 2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
