# SCC_SetNominalVoltage

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetNominalVoltage ( float NominalVoltage )
```

## Description

Sets lower limits and other electrical values for the message ChargeParameterDiscoveryRes. These limits are used in various messages for both AC and DC mode (the actual element name depends on the charging mode and the procotol version). Defaults can be set using the respective configuration file.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
