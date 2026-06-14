# SCC_SLAC_SetChipPresent

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SLAC_SetChipPresent ( dword ChipPresent )
```

## Description

Configures the SLAC protocol to run with a real QCA7000 chip, or without it. This toggles the sending of artificial attenuation data.

This function overrides the configuration parameter <SLAC_ChipPresent>. The supplied EV / EVSE configurations for VT8770 are already configured to use a real chip - there is no need to adapt these.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
