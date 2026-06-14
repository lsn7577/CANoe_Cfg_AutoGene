# GNSSSetJitterLatLon

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetJitterLatLon( double jitter )
```

## Description

This function sets the jitter by which the longitudinal and latitudinal degree deviates from the respective nominal value. The unit of the parameter depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

error code

## Example

```c
double jitter = 1.5;
GNSSSetUnits( 0 );
GNSSSetJitterLatLon( jitter ); // 1.5 
 m
```

## Availability

| Since Version |
|---|
