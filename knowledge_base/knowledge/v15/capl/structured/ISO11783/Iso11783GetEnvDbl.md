# Iso11783GetEnvDbl

> Category: `ISO11783` | Type: `function`

## Syntax

```c
double Iso11783GetEnvDbl( char envVar[], dword index );
```

## Description

This function gets the value of an environment variable.

## Parameters

| Name | Description |
|---|---|
| envVar | Name of the environment variable |
| index | Index of the environment variable |

## Return Values

Value of the environment variable or 0.0 if it does not exist

## Example

```c
value 
 = Iso11783GetEnvDbl( „EvFrictionForce“, 
 1 );
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
