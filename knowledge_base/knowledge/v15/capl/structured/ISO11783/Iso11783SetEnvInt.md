# Iso11783SetEnvInt

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783SetEnvInt( char envVar[], dword index, dword value );
```

## Description

This function sets the value of an environment variable.

## Parameters

| Name | Description |
|---|---|
| envVar | Name of the environment variable |
| index | Index of the environment variable |
| value | New value |

## Return Values

0 on success or error code

## Example

```c
Iso11783SetEnvInt( „EvFrictionForce“, 
 1, 3 );
```

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
