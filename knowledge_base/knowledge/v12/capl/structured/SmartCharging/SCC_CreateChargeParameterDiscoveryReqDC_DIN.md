# SCC_CreateChargeParameterDiscoveryReqDC_DIN

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateChargeParameterDiscoveryReqDC_DIN ( byte SessionID[], byte StatusFlags[], char ErrorCode[], char EnergyTransferType[], float MaxCurrent, float MaxVoltage)
```

## Description

Creates a Charge Parameter Discovery Request message for sending, using the DC syntax.

## Return Values

1 if successful

## Availability

| Since Version |
|---|
