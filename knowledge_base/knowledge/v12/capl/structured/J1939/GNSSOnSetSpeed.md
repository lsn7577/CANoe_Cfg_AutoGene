# GNSSOnSetSpeed

> Category: `J1939` | Type: `function`

## Syntax

```c
void GNSSOnSetSpeed( double speed )
```

## Description

This function is called if the speed of the simulation has been changed. This is helpful in the case of simulation by a file when the speed is determined from the file (see GNSSStartSimulation).

The unit of the parameter depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

—

## Example

```c
void GNSSOnSetSpeed( double speed )
{
  write(“New speed = %lf”, speed )
}
```

## Availability

| Since Version |
|---|
