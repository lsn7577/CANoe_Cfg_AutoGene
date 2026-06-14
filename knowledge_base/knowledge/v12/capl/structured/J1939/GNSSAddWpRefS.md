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

| Since Version |
|---|
