# AfdxGetTokenLengthBit

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetTokenLengthBit( long packet, char protocolDesignator[], char tokenDesignator[] );
```

## Description

This function returns the length of a token in bit.

## Parameters

| Name | Description |
|---|---|
| packet | handle of the message that has been created with AfdxInitPacket |
| protocolDesignator | name of the protocol, e.g. "afdx" |
| tokenDesignator | name of the token, e.g. "header" |

## Return Values

length of the token in bit
With AfdxGetLastError you have to check if the function has been processed successfully.

## Example

```c
long packet = 0;
long len = 0;
char error[100];

packet = AfdxInitPacket( "afdx" );
len = AfdxGetTokenLengthBit( packet, "afdx", "data" );
if (AfdxGetLastError() == 0)
{
  // do something with len
}
else
{
  AfdxGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
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
