# GNSSSetCourse

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetCourse( double course, double gradient )
```

## Description

This function determines the new course and the new gradient at which the GNSS receiver will continue its motion. These two values are only used in kCourse simulation mode (see GNSSStartSimulation).

The following table describes the relationship between course and compass direction:

0°

North

90°

East

180°

South

270°

West

If this function is called, previously set waypoints (e.g. by function GNSSAddWpMeander or GNSSAddWpRel) are ignored.

## Return Values

error code

## Example

```c
double c = 90.0, g = 0.0;
GNSSSetCourse( c, g );
```

## Availability

| Since Version |
|---|
