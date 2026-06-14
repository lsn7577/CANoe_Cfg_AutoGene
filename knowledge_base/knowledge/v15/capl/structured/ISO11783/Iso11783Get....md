# Iso11783Get...

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783GetAAC( char[] deviceName );
long Iso11783GetIG( char[] deviceName );
long Iso11783GetVS( char[] deviceName );
long Iso11783GetVSInstance( char[] deviceName );
long Iso11783GetFct( char[] deviceName );
long Iso11783GetFctInstance( char[] deviceName );
long Iso11783GetECUInstance( char[] deviceName );
long Iso11783GetMC( char[] deviceName );
long Iso11783GetIN( char[] deviceName );
```

## Description

This function reads a part of the device name.

## Parameters

| Name | Description |
|---|---|
| deviceName | Buffer for read part of the device name, minimum size of 8 bytes required |

## Return Values

Value of the device name part

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | Iso11783 | Iso11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
