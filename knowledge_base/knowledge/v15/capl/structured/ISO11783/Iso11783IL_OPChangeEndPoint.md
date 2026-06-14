# Iso11783IL_OPChangeEndPoint

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeEndPoint( dword objectID, dword width, dword height, dword direction ); // form 1
long Iso11783IL_OPChangeEndPoint( dbNode implement, dword objectID, dword width, dword height, dword direction ); // form 2
```

## Description

The function changes the length and alignment of a line object. A Change End Point command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| objectID | Object ID of the line object |
| width | Width of the bounding rectangle of the object |
| height | Height of the bounding rectangle of the object |
| direction | Alignment of the line 0: from top/left to bottom/right 1: from bottom/left to top/right |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPChangeEndPoint( 1200, 50, 20, 0 );
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
