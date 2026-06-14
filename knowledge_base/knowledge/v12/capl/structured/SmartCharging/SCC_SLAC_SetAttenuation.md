# SCC_SLAC_SetAttenuation

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SLAC_SetAttenuation ( float AttenuationMean, float AttenuationDev )
```

## Description

Changes the probability distribution used to create attenuation characteristics when simulating a QCA chip. The values apply to all SLAC sessions, yet may be set each time an M-Sound is received using the indication SCC_CM_MNBC_Sound_Ind.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
