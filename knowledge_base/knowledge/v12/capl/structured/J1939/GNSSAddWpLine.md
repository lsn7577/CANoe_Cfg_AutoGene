# GNSSAddWpLine

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpLine( double latitude1, double longitude1, double altitude1, double latitude2, double longitude2, double altitude2,dword straightLine)
```

## Description

This function can be used to describe a line. To do this, the points that describe the line are inserted at the end of the waypoint list.

StraightLine = 1

The beginning and end points are connected by a straight line. In the case of an extended distance, the altitude with respect to the earth ellipsoid changes because of the curvature of the earth. The same result can be obtained by adding two individual way-points (for example with GNSSAddWp).

StraightLine = 0

To keep the altitude approximately constant, a number of intermediate points are used by the function. The fixed distance between these intermediate points is about 1000m.

The unit of the parameters altitude1 and altitude2 depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

error code

## Example

```c
GNSSAddWpLine( 54.0, 8.0, 0.0, 54.2, 7.9, 0.0, 1 );
```

## Availability

| Since Version |
|---|
