# GNSSAddWpRefS

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpRefS( double latLength, double lonLength, double altLength, double speed )
```

## Description

This function inserts a new waypoint at a given speed at the end of the waypoint list. The new point is derived by adding the path differences and the last waypoint to be set by GNSSSetRefPoint.

When the new waypoint is reached, the GNSS receiver moves on at the assigned speed. The speed will be maintained until a waypoint with another speed is reached or the speed is changed by the GNSSSetSpeed function.

The unit of the parameters depends on the system of measurement units selected with the GNSSSetUnits function.

## Parameters

| Name | Description |
|---|---|
| latLength | difference in length along the latitude in respect to the reference point (in m or yd) positive value: eastward negative value: westward |
| lonLength | difference in length along the longitude in respect to the reference point (in m or yd) positive value: northward negative value: southward |
| altLength | difference in altitude with respect to the reference point (in m or yd) |
| speed | speed of the GNSS receiver (in km/h, mph or kn) |

## Return Values

error code

## Example

```c
// set a reference point
GNSSSetRefPoint( 48.46, 9.11, 225 ) ; 

// add a new waypoint 50 yd southerly and 
 30 yd westerly of the reference point and set a new speed of 35 mph when 
 this waypoint is reached
GNSSSetUnits( 1 );
GNSSAddWpRefS( -30.0, -50.0, 0, 35 );
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
