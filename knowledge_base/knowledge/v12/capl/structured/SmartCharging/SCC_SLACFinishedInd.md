# SCC_SLACFinishedInd

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_SLACFinishedInd ( dword Result )
```

## Description

The callback is called when a SLAC run has been completed. It marks the point in time when the SECC Discovery process can be started, if a match has been found and as soon as the link is established.

The vehicle can use the function SCC_SLAC_GetAttenResults during this callback to get the measured attenuation values.

## Return Values

—

## Availability

| Since Version |
|---|
