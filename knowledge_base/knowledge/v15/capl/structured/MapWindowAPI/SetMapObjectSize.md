# SetMapObjectSize

> Category: `MapWindowAPI` | Type: `function`

## Syntax

```c
long SetMapObjectSize( long handle, float size ); // form 1
long SetMapObjectSize( long handle, float width, float height ); // form 2
```

## Description

Sets either the size (form 1) or the height and width (form 2) of a map object.

## Parameters

| Name | Description |
|---|---|
| handle | Reference of the map object. |
| size | Size of the map object in meters. |
| width | Width of the map object in meters. |
| height | Height of the map object in meters. |

## Example

See Map Window API example.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | — | — | 14 | 5.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | ✔ | N/A |
| 32-Bit | — | ✔ | — | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | — | — | ✔ | N/A |
