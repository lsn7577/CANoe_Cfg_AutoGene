# GBT27930IL_GetLastError

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_GetLastError(); // form 1
long GBT27930IL_GetLastError(dbNode node); // form 2
```

## Description

Gets the return value of the last called GBT27930 IL function.

## Parameters

| Name | Description |
|---|---|
| node | Simulation node to apply the function |

## Example

```c
on key 't'
{
  BYTE date = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06 };
  GBT27930IL_SetSignalRaw( EEC1::EngSpeed, 6, data );
  write( "Errorcode = %d", GBT27930IL_GetLastError() );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 and Smart Charging | J1939 and Smart Charging | — | — | form 2 J1939 and Smart Charging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
