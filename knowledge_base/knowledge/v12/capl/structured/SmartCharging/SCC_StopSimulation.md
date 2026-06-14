# SCC_StopSimulation

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_StopSimulation ( )
```

## Description

These functions activate/deactivate the SCC simulation.

If the simulation is deactivated, no messages are sent and the API (except SCC_StartSimulation()) has no effect!

With the vehicle DLL, the call of SCC_StartSimulation() starts the setup of a connection.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
