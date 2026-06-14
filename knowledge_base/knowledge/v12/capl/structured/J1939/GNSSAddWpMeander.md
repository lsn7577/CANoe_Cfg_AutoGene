# GNSSAddWpMeander

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpMeander( double latitudeRef, double longitudeRef, double altitudeRef, double width, double height, double radius, dword numOfLoops);
```

## Description

This function can be used to describe a meander with rounded off corners. To do this, the points that describe the meander are inserted at the end of the waypoint list. The unit of the parameters depends on the system of measurement units selected with the GNSSSetUnits function.

The following illustrations describe the effect of the prefixed sign on the values for height and width (assuming that radius = 0). The thicker point identifies the reference point.

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

| Since Version |
|---|
