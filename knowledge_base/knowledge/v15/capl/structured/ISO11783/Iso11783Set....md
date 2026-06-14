# Iso11783Set...

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783SetAAC( char[] deviceName, long aac);
long Iso11783SetIG( char[] deviceName, long ig);
long Iso11783SetVS( char[] deviceName, long vs);
long Iso11783SetVSInstance( char[] deviceName, long vsi);
long Iso11783SetFct( char[] deviceName, long fct);
long Iso11783SetFctInstance( char[] deviceName, long fct );
long Iso11783SetECUInstance( char[] deviceName, long ecui );
long Iso11783SetMC( char[] deviceName, long mc);
long Iso11783SetIN( char[] deviceName, long in);
```

## Description

The function modifies a part of the device name.

## Parameters

| Name | Description |
|---|---|
| deviceName | Buffer containing the modified part of the device name, size of 8 bytes required |

## Return Values

0 or error code

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
