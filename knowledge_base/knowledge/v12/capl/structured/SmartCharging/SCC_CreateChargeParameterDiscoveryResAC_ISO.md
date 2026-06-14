# SCC_CreateChargeParameterDiscoveryResAC_ISO

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateChargeParameterDiscoveryResAC_ISO ( byte SessionID[], char ResponseCode[], long NotificationMaxDelay, byte StatusFlags[], char Notification[], long EVSEProcessing, float NominalVoltage, float MaxCurrent )
```

## Description

Creates a Charge Parameter Discovery Response message for sending, using the AC syntax.

## Return Values

1 if successful

## Availability

| Since Version |
|---|
