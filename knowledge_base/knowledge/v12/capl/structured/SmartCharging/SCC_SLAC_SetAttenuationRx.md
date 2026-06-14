# SCC_SLAC_SetAttenuationRx

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SLAC_SetAttenuationRx ( float AttenuationRx )
```

## Description

Sets the attenuation of the Rx path, which is subtracted from the AAG values. This is can also be used to influence the calculation of attenuation values when a real chip is used, i.e. the attenuation may be artificially raised or lowered.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
