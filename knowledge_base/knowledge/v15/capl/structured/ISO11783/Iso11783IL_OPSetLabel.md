# Iso11783IL_OPSetLabel

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPSetLabel( dword objectID, dword stringVarIdD, dword fontType, dword graphID ); // form 1
long Iso11783IL_OPSetLabel( dbNode implement, dword objectID, dword stringVarIdD, dword fontType, dword graphID ); // form 2
```

## Description

A Set Label command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| objectID | object ID which is assigned to the label |
| stringVarID | object ID of the string variable object |
| fontType | font type |
| graphID | object ID of a graphical object |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPSetLabel( 
 1200, 1250, 1, 1260 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1 9.0: form 2 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
