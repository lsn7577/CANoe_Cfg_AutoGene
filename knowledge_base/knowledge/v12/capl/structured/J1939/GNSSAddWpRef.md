# GNSSAddWpRef

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpRef( double latLength, double lonLength, double altLength )
```

## Description

This function inserts a new waypoint at the end of the waypoint list. The new point is derived by adding the path differences and the last waypoint to be set by GNSSSetRefPoint.

The unit of the parameters depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

error code

## Example

```c
// set reference point
GNSSSetRefPoint( 48.46, 9.11, 255.0 ) ; 

// add a new waypoint 150 meter northly 
 of the reference point
GNSSSetUnits( 0 );
GNSSAddWpRef( 0.0, 150.0, 0.0 );
```

## Availability

| Since Version |
|---|
