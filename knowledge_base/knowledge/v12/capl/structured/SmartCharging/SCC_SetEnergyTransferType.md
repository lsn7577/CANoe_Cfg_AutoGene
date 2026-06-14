# SCC_SetEnergyTransferType

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetEnergyTransferType ( char EnergyTransferType[] ) //form 1 (EV only)
```

## Description

EV:

Sets the desired charging mode for a running SCC session. For the list of all valid charging modes, see the SCC specification.

EVSE:

Sets the offered energy transfer type (DIN 70121) resp. -mode (ISO 15118) for a running SCC session. In case of ISO 15118, a list with one element is created. For the list of all valid values, see the SCC specification.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
