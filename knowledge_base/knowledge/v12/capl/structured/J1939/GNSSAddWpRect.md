# GNSSAddWpRect

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpRect( double latitudeRef, double longitudeRef, double altitudeRef, double width, double height, double radius );
```

## Description

This function can be used to describe a rectangle with rounded off corners. To do this, the points that describe the rectangle are inserted at the end of the waypoint list. The unit of the parameters depends on the system of measurement units selected with the GNSSSetUnits function.

The following illustrations describe the effect of the prefixed sign on the values for height and width (assuming that radius = 0). The thicker point identifies the reference point.

Special case: If the height and width are both identical to one half the radius, the result is a circle.

## Return Values

error code

## Example

```c
// slotted hole with width of 400 yd and 
 height of 200 yd
GNSSSetUnits( 1 );
GNSSAddWpRect( 48.46, 9.11, 225, 400, 200, 100 
 );
```

## Availability

| Since Version |
|---|
