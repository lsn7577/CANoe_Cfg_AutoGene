# SetMapObjectPosition

> Category: `MapWindowAPI` | Type: `function`

## Syntax

```c
long SetMapObjectPosition( long handle, float latitude1, float longitude1 ); // form 1
long SetMapObjectPosition( long handle, float latitude1, float longitude1, float latitude2, float longitude2 ); // form 2
```

## Description

Sets the GPS position of a map object either for one (form 1) or two (form 2) points.

## Parameters

| Name | Description |
|---|---|
| handle | Reference of the map object. |
| latitude1 | First latitude value of the map object to be drawn. |
| longitude1 | Frst longitude value of the map object to be drawn. |
| latitude2 | Second latitude value of the map object to be drawn (needed for drawing lines). |
| longitude2 | Second longitude value of the map object to be drawn (needed for drawing lines). |

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
