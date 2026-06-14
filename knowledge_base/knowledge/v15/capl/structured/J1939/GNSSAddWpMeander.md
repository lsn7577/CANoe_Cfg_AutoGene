# GNSSAddWpMeander

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpMeander( double latitudeRef, double longitudeRef, double altitudeRef, double width, double height, double radius, dword numOfLoops);
```

## Description

This function can be used to describe a meander with rounded off corners. To do this, the points that describe the meander are inserted at the end of the waypoint list. The unit of the parameters depends on the system of measurement units selected with the GNSSSetUnits function.

The following illustrations describe the effect of the prefixed sign on the values for height and width (assuming that radius = 0). The thicker point identifies the reference point.

## Parameters

| Name | Description |
|---|---|
| latitudeRef | latitude of the reference point (in degrees) |
| longitudeRef | longitude of the reference point (in degrees) |
| altitudeRef | altitude of the reference point (in m or ft) |
| width | width (w) of a loop (in m or yd). Direction is west to east or east to west. |
| height | height (h) of a loop (in m or yd). Direction is north to south or south to north. |
| radius | radius (r) of the rounded off corners of the loop (in m or yd) |
| numOfLoops | number of loops |

## Return Values

error code

## Example

```c
// meander with 3 loops, every loop has 
 a width of 100 yd and a height of 200 yd
GNSSSetUnits( 1 );
GNSSAddWpMeander( 48.46, 9.11, 225, 100, 200, 
 10, 3 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | — |
| Restricted To | — | J1939 ISO11783 | J1939 ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
