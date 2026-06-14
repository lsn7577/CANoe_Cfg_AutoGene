# J1939SetEnvDbl

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939SetEnvDbl( char envVar[], dword index, float value );
```

## Description

This function sets the value of an environment variable.

## Parameters

| Name | Description |
|---|---|
| envVar | name of the environment variable |
| index | index of the environment variable |
| value | new value |

## Return Values

0 on success or error code

## Example

```c
J1939SetEnvDbl( "EvFrictionForce", 
 1, 33.12 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
