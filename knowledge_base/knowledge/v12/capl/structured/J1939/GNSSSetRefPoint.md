# GNSSSetRefPoint

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetRefPoint( double latitude, double longitude, double altitude )
```

## Description

This function defines a reference point that will be used by the functions GNSSAddWpRef and GNSSAddWpRefS to calculate a new waypoint. The unit of the altitude parameter depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

error code

## Example

```c
GNSSSetRefPoint( 48.46, 9.11, 225.0 );
```

## Availability

| Since Version |
|---|
