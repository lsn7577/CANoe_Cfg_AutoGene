# linActivateGlobalNetworkManagement

> Category: `LIN` | Type: `function`

## Syntax

```c
long linActivateGlobalNetworkManagement(long active)
```

## Description

Activates/deactivates network management for the entire LIN network (the channel is determined by the CAPL program context).

Network management is responsible for the automatic setting and resetting of response error signals in the simulated Slave nodes.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
