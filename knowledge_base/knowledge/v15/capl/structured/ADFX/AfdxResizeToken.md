# AfdxResizeToken

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxResizeToken( long packet, char protocolDesignator[], char tokenDesignator[], long newBitLength );
```

## Description

This function sets the length of a token.

This function sets the length of a token and can only be used with resizable tokens ("header" and "data"). If a token is not resizable the error code 46-0125 is returned. The main purpose for this function is to create AFDX message with or without sequence number field. Calling the function with (n = number of bytes)

results in a "data" field size of n bytes. Additionally the sequence number field is located after the data field.

Calling the function with (n = number of bytes)

again results in a "data" field size of n bytes. In this case there is no sequence number field considered.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket. |
| protocolDesignator | Name of the protocol, e.g. "afdx" or "udp". |
| tokenDesignator | Name of the token, e.g. "data". |
| newBitLength | New length of the token in bits. |

## Example

```c
long packet;
long packetlen = 60;

packet = AfdxInitPacket(0x0a022600, 0xe0e01a0f, 11121, 0x1a0f, 640 );
packetlen = sysGetVariableInt( "%NODE_NAME%", "OutputPacketLength" );

// adapt frame size with an additional seqNo byte
AfdxResizeToken( packet, "afdx", "data", packetlen*8  );
AfdxCompletePacket(packet);
AfdxOutputPacket(packet);
AfdxReleasePacket(packet);
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
