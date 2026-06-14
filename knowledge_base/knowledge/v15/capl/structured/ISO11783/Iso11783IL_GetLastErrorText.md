# Iso11783IL_GetLastErrorText

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_GetLastErrorText( dword bufferSize, char buffer[] ); // form 1: deprecated.
long Iso11783IL_GetLastErrorText( char buffer[] ); // form 2
long Iso11783IL_GetLastErrorText( dbNode node, dword bufferSize, char buffer[] ); // form 3: deprecated.
long Iso11783IL_GetLastErrorText( dbNode node, char buffer[] ); // form 4
```

## Description

Returns the result of the last called ISO11783 IL function as string.

## Parameters

| Name | Description |
|---|---|
| bufferSize | size of the return buffer |
| buffer | return buffer |
| node | Simulation node to apply the function. |

## Example

```c
on key 't' 
{
  char error[64];
  BYTE date = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06 };
  ISO11783ILSetSignalRaw( EEC1::EngSpeed, 6, data );

  Iso11783IL_GetLastErrorText( error );
  write( "Errorcode:  %s", error );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 2) | ✔ (form 2 | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 4) | ✔ (form 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 4) | ✔ (form 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
