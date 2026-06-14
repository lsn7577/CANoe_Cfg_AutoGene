# GNSSGetCurSpeed

> Category: `J1939` | Type: `function`

## Syntax

```c
double GNSSGetCurSpeed();
```

## Description

This function returns the current speed at which the GNSS receiver is moving. If a value of 0.0 is returned, the GNSSGetLastError function must be used to check whether the value is valid.

The unit of the parameter depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

current speed (in km/h, mph or kn)

## Example

```c
double speed;
GNSSSetUnits( 0 );
speed = GNSSGetCurSpeed();
write(“Speed = %lf km/h”, speed);
```

## Availability

| Since Version |
|---|
