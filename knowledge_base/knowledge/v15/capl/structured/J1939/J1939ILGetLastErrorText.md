# J1939ILGetLastErrorText

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILGetLastErrorText(dword bufferSize, char buffer[] ); // form 1
long J1939ILGetLastErrorText(dbNode node, dword bufferSize, char buffer[] ); // form 2
```

## Description

Returns the result of the last called J1939 IL function as string.

## Parameters

| Name | Description |
|---|---|
| bufferSize | size of the return buffer |
| buffer | return buffer |
| node | Simulation node to apply the function |

## Example

```c
on key 't' 
{
  char error[64];
  BYTE date = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06 };
  J1939ILSetSignalRaw( EEC1::EngSpeed, 6, data );

J1939ILGetLastErrorText( error );
  write( "Errorcode:  %s", error );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2: form 1 12.0: form 2 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 | J1939 | — | — | form 2 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
