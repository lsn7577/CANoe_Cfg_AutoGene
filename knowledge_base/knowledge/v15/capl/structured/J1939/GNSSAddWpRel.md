# GNSSAddWpRel

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpRel( double latLength, double lonLength, double altLength )
```

## Description

This function inserts a new waypoint at the end of the waypoint list. The new point is derived by adding the path differences and the last waypoint to be inserted.

The unit of the parameters depends on the system of measurement units selected with the GNSSSetUnits function.

## Parameters

| Name | Description |
|---|---|
| latLength | difference in length along the latitude in reference to the last waypoint to be inserted (in m or yd) positive value: eastward negative value: westward |
| lonLength | difference in length along the longitude in reference to the last waypoint to be inserted (in m or yd) positive value: northward negative value: southward |
| altLength | difference in altitude in terms of the last waypoint to be inserted (in m or yd) |

## Return Values

error code

## Example

```c
// set a waypoint
GNSSAddWp( 48.46, 9.11, 255 ) ; 

// add a new waypoint 200 yd easterly of 
 the last waypoint
GNSSSetUnits( 1 );
GNSSAddWpRel( 200.0, 0.0, 0.0 );
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
