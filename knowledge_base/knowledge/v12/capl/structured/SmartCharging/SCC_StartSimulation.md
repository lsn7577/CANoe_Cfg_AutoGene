# SCC_StartSimulation

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_StartSimulation ( ) // form 1
```

## Description

These functions start the simulation DLL in active mode.

Until the simulation is started, no messages are sent and the API (except SCC_StartSimulation()) has no effect!

With the vehicle DLL, the call of SCC_StartSimulation() starts the setup of a connection.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
