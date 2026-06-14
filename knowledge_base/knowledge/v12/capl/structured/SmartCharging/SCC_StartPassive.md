# SCC_StartPassive

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
SCC_StartPassive(SLACMode);
```

## Description

This function activates the Nodelayer DLL, but does not start an SCC simulation (i.e. a state machine). In this state, callbacks can be received, and test functions can be called.

## Parameters

| Name | Description |
|---|---|
| SLACMode | Controls the behavior regarding SLAC, which overrides the parameter <UseSLAC> from the XML configuration: |

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
