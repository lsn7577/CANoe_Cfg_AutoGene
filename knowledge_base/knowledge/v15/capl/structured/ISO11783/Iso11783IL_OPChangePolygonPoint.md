# Iso11783IL_OPChangePolygonPoint

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangePolygonPoint( dword polygonID, dword index, dword x, dword y ); // form 1
long Iso11783IL_OPChangePolygonPoint( dbNode implement, dword polygonID, dword index, dword x, dword y ); // form 2
```

## Description

The function changes the position of a point of a polygon object. A Change Polygon Point command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| polygonID | Object ID of a polygon object |
| index | Index of the point |
| x | X position |
| y | Y position |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPChangePolygonPoint( 1200, 2, 25, 10 );
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
