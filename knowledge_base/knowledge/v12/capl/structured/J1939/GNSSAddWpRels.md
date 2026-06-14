# GNSSAddWpRels

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpRels( double latLength, double lonLength, double altLength, double speed )
```

## Description

This function inserts a new waypoint at a given speed at the end of the waypoint list. The new point is derived by adding the path differences and the last waypoint to be inserted.

When the new waypoint is reached, the GNSS receiver moves on at the assigned speed. The speed will be maintained until a waypoint with another speed is reached or the speed is changed by the GNSSSetSpeed function.

The unit of the parameters depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

error code

## Example

```c
// set a waypoint
GNSSAddWaypoint( 54.0, 8.0, 0 ) ; 

// add a new waypoint 200 yd southerly 
 of the last waypoint and set a new speed of 10 kn when this waypoint is 
 reached
GNSSSetUnits( 2 );
GNSSAddWpRels( 0.0, -200.0, 0, 10 );
```

## Availability

| Since Version |
|---|
