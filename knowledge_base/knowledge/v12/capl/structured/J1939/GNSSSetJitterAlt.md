# GNSSSetJitterAlt

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetJitterAlt( double jitter )
```

## Description

This function sets the jitter by which the altitude deviates from its nominal value. The unit of the parameter depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

error code

## Example

```c
double jitter = 0.7;
GNSSSetUnits( 1 );
GNSSSetJitterAlt( jitter ); // 0,7 
 yard
```

## Availability

| Since Version |
|---|
