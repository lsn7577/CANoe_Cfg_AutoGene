# Iso11783OPChangePolygonScale

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangePolygonScale( dword ecuHandle, dword polygonID, dword width, dword height );
```

## Description

The function changes the size of a polygon object. A Change Polygon Scale command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangePolygonScale( handle, 1200, 80, 40 );
```

## Availability

| Since Version |
|---|
