# GNSSAddWpRel

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpRel( double latLength, double lonLength, double altLength )
```

## Description

This function inserts a new waypoint at the end of the waypoint list. The new point is derived by adding the path differences and the last waypoint to be inserted.

The unit of the parameters depends on the system of measurement units selected with the GNSSSetUnits function.

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

| Since Version |
|---|
