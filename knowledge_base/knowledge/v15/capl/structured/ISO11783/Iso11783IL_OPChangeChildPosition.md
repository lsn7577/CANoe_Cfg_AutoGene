# Iso11783IL_OPChangeChildPosition

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeChildPosition( dword parentID, dword objectID, long x, long y ); // form 1
long Iso11783IL_OPChangeChildPosition( dbNode implement, dword parentID, dword objectID, long x, long y ); // form 2
```

## Description

The function changes the absolute position of an object inside its parent object. A Change Child Position command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| parentID | Parent object |
| objectID | Object which should change its position |
| x | Absolute X Position inside the parent object |
| y | Absolute Y Position inside the parent object |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPChangeChildPosition( 1000, 1200, 10, 10 );
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
