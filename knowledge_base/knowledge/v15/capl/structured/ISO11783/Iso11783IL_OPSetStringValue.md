# Iso11783IL_OPSetStringValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPSetStringValue( dword objectID, char stringValue[] ); // form 1
long Iso11783IL_OPSetStringValue( dword objectID, char stringValue[], dword options ); // form 2
long Iso11783IL_OPSetStringValue( dbNode implement, dword objectID, char stringValue[], dword options ); // form 3
```

## Description

The functions set the string value of an object in the object pool. The object must exist in the object pool and must support a string value. If the Object Pool API is active, a Change String Value command is sent to the Virtual Terminal. This can be suppressed with Bit 0 in options.

## Parameters

| Name | Description |
|---|---|
| objectID | object ID of the object that has an updated value |
| stringValue | buffer containing new string value |
| options | options Bit 0 and 1 = 0: send Change String Value command if parameters are valid Bit 0 and 1 = 1: suppress Change String Value command Bit 0 and 1 = 2: force sending Change String Value command even parameters are invalid Bit 0 and 1 = 3: reserved |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPSetStringValue( 1000, “Hello World” );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2 9.0: form 3 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3) | ✔ (form 3) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3) | ✔ (form 3) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
