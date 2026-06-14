# Iso11783IL_OPChangePolygonPoint

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangePolygonPoint( dword polygonID, dword index, dword x, dword y ); // form 1
```

## Description

The function changes the position of a point of a polygon object. A Change Polygon Point command is sent to the Virtual Terminal.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPChangePolygonPoint( 1200, 2, 25, 10 );
```

## Availability

| Since Version |
|---|
