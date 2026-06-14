# Iso11783IL_OPChangePolygonScale

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangePolygonScale( dword polygonID, dword width, dword height ); // form 1
```

## Description

The function changes the size of a polygon object. A Change Polygon Scale command is sent to the Virtual Terminal.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPChangePolygonScale( 1200, 80, 40 );
```

## Availability

| Since Version |
|---|
