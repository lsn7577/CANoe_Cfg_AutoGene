# AfdxSetTokenData

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length, byte buffer[] ); // form 1
long AfdxSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length, char buffer[] ); // form 2
long AfdxSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length, struct * buffer ); // form 3
```

## Description

This function copies a number of bytes from source buffer to a token's data area. The token is not resized. Use AfdxResizeToken to change the token's length.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket. |
| protocolDesignator | Name of the protocol, e.g. "afdx". |
| tokenDesignator | Name of the token, e.g. "source". |
| offset | This is the offset from the beginning of the token's data area. If this is 0, data is copied starting at byte 0 of the token's data area. |
| length | This is the number of bytes to be copied from the specified buffer to the token's data area. Note that the token is not resized. Make sure that the token's size is at least length bytes. |
| buffer | This is the source buffer for the copied data. |

## Example

see example of AfdxInitPacket

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2, 3 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
