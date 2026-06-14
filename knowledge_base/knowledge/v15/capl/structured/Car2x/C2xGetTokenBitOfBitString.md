# C2xGetTokenBitOfBitString

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetTokenBitOfBitString( long packet, char protocolDesignator[], char tokenDesignator[], char namedBit[] ); // form 1
long C2xGetTokenBitOfBitString( long packet, char protocolDesignator[], char tokenDesignator[], long bitPosition ); // form 2
```

## Description

This function gets the value of a bit in a bit string that is specified either by its name (form 1) or by its position (form 2).

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket |
| protocolDesignator | Name of the protocol, e.g. geo_cnh |
| tokenDesignator | Name of the token, e.g. data |
| namedBit | Name of the bit |
| bitPosition | Zero based index of the bit |

## Return Values

Value of the bit.

## Example

See example of C2xSetTokenBitOfBitString.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 SP4 | — | — | — | 2.1 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
