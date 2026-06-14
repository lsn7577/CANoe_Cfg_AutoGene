# AfdxSetTokenInt64

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetTokenInt64( long packet, char protocolDesignator[], char tokenDesignator[], int64 value ); // form 1
long AfdxSetTokenInt64( long packet, char protocolDesignatorl[], char tokenDesignator[], long offset, long length, long networkByteOrder, int64 value ); // form 2
```

## Description

This function sets the specified token‘s data to a new 64-bit integer value. With additional parameters (form 2) the user may specify the starting byte, length and byte ordering of the integer value in the token.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket. |
| protocolDesignator | Name of the protocol, e.g. "afdx". |
| tokenDesignator | Name of the token, e.g. "lpvSpeed". |
| offset | This is the offset from the beginning of the token's data area. If this is 0, data is copied starting at byte 0 of the token's data area. |
| length | This is the length of the integer value to be copied to the token's data area (range 1..8). |
| networkByteOrder | 0: INTEL (little-endian) 1: MOTOROLA (big-endian) |
| value | New integer value. |

## Example

see example of AfdxInitPacket

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
