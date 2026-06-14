# GNSSStartSimulation

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSStartSimulation( dword simType )
```

## Description

This function starts the simulation. At least one waypoint must be set for a start to be successful.

Simulation modes:

## Return Values

error code

## Example

```c
if ( GNSSStartSimulation(0) == 0 ) {
  write("Start simulation");
}
```

## Availability

| Since Version |
|---|
