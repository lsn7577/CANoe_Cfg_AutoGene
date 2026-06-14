# GNSSSetCourse

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetCourse( double course, double gradient )
```

## Description

This function determines the new course and the new gradient at which the GNSS receiver will continue its motion. These two values are only used in kCourse simulation mode (see GNSSStartSimulation).

The following table describes the relationship between course and compass direction:

If this function is called, previously set waypoints (e.g. by function GNSSAddWpMeander or GNSSAddWpRel) are ignored.

## Parameters

| Name | Description |
|---|---|
| course | the course in degrees |
| gradient | the inclination in degrees |

## Return Values

error code

## Example

```c
double c = 90.0, g = 0.0;
GNSSSetCourse( c, g );
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
