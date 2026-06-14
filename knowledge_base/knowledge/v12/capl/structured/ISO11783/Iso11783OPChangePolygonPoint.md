# Iso11783OPChangePolygonPoint

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangePolygonPoint( dword ecuHandle, dword polygonID, dword index, dword x, dword y );
```

## Description

The function changes the position of a point of a polygon object. A Change Polygon Point command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangePolygonPoint( handle, 1200, 2, 25, 10 );
```

## Availability

| Since Version |
|---|
