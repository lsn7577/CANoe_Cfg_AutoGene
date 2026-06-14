# SetMapObjectFillColor

> Category: `MapWindowAPI` | Type: `function`

## Syntax

```c
long SetMapObjectFillColor( long handle, float fillColor );
```

## Description

Sets the fill color of a map object or the text color of a text object.

## Parameters

| Name | Description |
|---|---|
| handle | Reference of the map object. |
| Note makeRGB Up to and including CANoe version 12.0 SP2, the function makeRGB returned the blue value in the second byte and the red value in the fourth byte.Functions that received this value as a parameter interpreted this exchange so that the color was displayed correctly. From CANoe 12.0 SP3, the function makeRGB returns the color values in the correct order.Functions that have received this value as a parameter have also been adjusted to display the correct color again. Existing programs only need to be adapted if you have not used the function makeRGB but you have passed the color hard coded. |  |

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
