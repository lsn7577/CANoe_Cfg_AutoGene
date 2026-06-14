# C2xGetTokenLengthBit

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetTokenLengthBit( long packet, char protocolDesignator[], char tokenDesignator[] );
```

## Description

This function returns the length of a token in bit.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket |
| protocolDesignator | Name of the protocol, e.g. geo_cnh |
| tokenDesignator | Name of the token, e.g. header |

## Return Values

Length of the token in bit
With C2xGetLastError you can check if the function has been processed successfully.

## Example

```c
long packet = 0;
long len = 0;
char error[100];

packet = C2xInitPacket( "geo_cnh" );
len    = C2xGetTokenLengthBit( packet, "geo_cnh", "header" ); // = 32

if (C2xGetLastError() == 0)
{
  // do something with len
}
else
{
  C2xGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
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
