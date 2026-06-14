# GNSSGetCurGradient

> Category: `J1939` | Type: `function`

## Syntax

```c
double GNSSGetCurGradient();
```

## Description

This function returns the current gradient in degrees at which the GNSS receiver is moving.

If a value of 0.0 is returned, the GNSSGetLastError function must be used to check whether the value is valid (see error codes).

## Return Values

current gradient in degrees

## Example

Example

```c
double gradient;
gradient = GNSSGetCurGradient();
write(“Gradient = %lf degree”, gradient);
```

## Availability

| Since Version |
|---|
