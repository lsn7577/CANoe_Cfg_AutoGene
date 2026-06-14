# Iso11783IL_OPGetStringValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPGetStringValue( dword objectID, dword bufferSize, char buffer[] ); // form 1: deprecated.
long Iso11783IL_OPGetStringValue( dword objectID, char buffer[] ); // form 2
long Iso11783IL_OPGetStringValue( dbNode implement, dword objectID, dword bufferSize, char buffer[] ); // form 3: deprecated.
long Iso11783IL_OPGetStringValue( dbNode implement, dword objectID, char buffer[] ); // form 4
```

## Description

The function copies a string value of an object in the object pool into a buffer. The object must exist in the object pool and support a string value.

## Parameters

| Name | Description |
|---|---|
| objectID | object Identifier of the object |
| bufferSize | size of the string buffer |
| buffer | string buffer in which the string is copied |
| implement | Simulation node to apply the function. |

## Example

```c
char buffer[100];
Iso11783IL_OPGetStringValue( 1000, buffer );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0: form 2, 4 | 13.0 | — | — | 5.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 4) | ✔ (form 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 4) | ✔ (form 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
