# VTIL_GetLastErrorText

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetLastErrorText( dword bufferSize, char buffer[] ); // form 1: deprecated.
long VTIL_GetLastErrorText( char buffer[] ); // form 2
long VTIL_GetLastErrorText( dbNode vt,dword bufferSize, char buffer[]); // form 3: deprecated.
long VTIL_GetLastErrorText( dbNode vt, char buffer[]); // form 4
```

## Description

Returns the result of the last VT IL function as string.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| bufferSize | size of the return buffer |
| buffer | return buffer |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 4) | ✔ (form 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 4) | ✔ (form 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
