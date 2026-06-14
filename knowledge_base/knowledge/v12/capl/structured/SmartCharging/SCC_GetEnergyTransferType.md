# SCC_GetEnergyTransferType

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_GetEnergyTransferType ( char[] EnergyTransferType )
```

## Description

Gets the energy transfer type (DIN 70121) resp. -mode (ISO 15118) from various messages.

## Return Values

Type of requested power supply:
AC_Charging = 0,
DC_Charging = 1
The EnergyTransferType resp -Mode string is additionally written to the output buffer. If this is not required, an empty string can be transferred.

## Availability

| Since Version |
|---|
