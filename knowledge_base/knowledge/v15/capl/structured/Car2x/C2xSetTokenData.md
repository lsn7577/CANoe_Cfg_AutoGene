# C2xSetTokenData

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, char data[] );
long C2xSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, byte data[] );
long C2xSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, struct dataStruct );
long C2xSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, char data[] );
long C2xSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, byte data[] );
long C2xSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, struct dataStruct );
```

## Description

This function sets the data or a part of data of a token.

It does not resize the token. Use C2xResizeToken to change the length.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket. |
| protocolDesignator | Name of the protocol, e.g. eth. |
| tokenDesignator | Name of the token, e.g. source. |
| byteOffset | Offset from the beginning of the token in byte. |
| length | Number of bytes to be copied. |
| data | Data that are copied to the token. |
| dataStruct | Struct containing the data. |

## Example

See example of C2xInitPacket.

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
