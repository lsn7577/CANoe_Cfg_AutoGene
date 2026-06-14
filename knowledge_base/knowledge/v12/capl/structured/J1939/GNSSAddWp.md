# GNSSAddWp

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWp( double latitude, double longitude, double altitude )
```

## Description

This function inserts a new waypoint at the end of the waypoint list. The unit of the altitude parameter depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

error code

## Example

```c
GNSSAddWp( 48.46, 9.11, 225.0 );
```

## Availability

| Since Version |
|---|
