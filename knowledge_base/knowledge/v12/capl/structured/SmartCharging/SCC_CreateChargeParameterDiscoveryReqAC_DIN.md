# SCC_CreateChargeParameterDiscoveryReqAC_DIN

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateChargeParameterDiscoveryReqAC_DIN ( byte SessionID[], char EnergyTransferType[], dword DepartureTime, float EAmount, float MaxVoltage, float MaxCurrent, float MinCurrent )
```

## Description

Creates a Charge Parameter Discovery Request message for sending, using the AC syntax.

## Return Values

1 if successful

## Availability

| Since Version |
|---|
