# GNSSRemoveWp

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSRemoveWp();
```

## Description

The function deletes all waypoints in the waypoint list that were added with GNSSAdd.... No waypoints can be deleted during a simulation.

## Return Values

error code

## Example

```c
GNSSStopSimulation();
GNSSRemoveWp();
```

## Availability

| Since Version |
|---|
