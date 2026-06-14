# GNSSAddWpS

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpS( double latitude, double longitude, double altitude, double speed )
```

## Description

This function inserts a new waypoint at a given speed at the end of the waypoint list. When this waypoint is reached, the GNSS receiver moves on at the assigned speed. The speed will continue to be used until a waypoint with another speed is reached or the speed is changed by the GNSSSetSpeed function.

The unit of the parameters speed and altitude depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

error code

## Example

```c
// stop GNSS receiver if the following 
 waypoint is reached
GNSSAddWpS( 48.46, 9.11, 255.0, 0 );
```

## Availability

| Since Version |
|---|
