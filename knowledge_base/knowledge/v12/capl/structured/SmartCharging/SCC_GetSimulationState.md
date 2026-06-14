# SCC_GetSimulationState

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_GetSimulationState ( )
```

## Description

This function checks if the simulation is running, waiting (in pause state) or stopped.

## Return Values

0: Simulation is deactivated
1: Simulation is running in passive mode
2: Simulation is running in active mode
3: Simulation is running in active mode and waiting
(SCC_SimulationWait() has been called)

## Availability

| Since Version |
|---|
