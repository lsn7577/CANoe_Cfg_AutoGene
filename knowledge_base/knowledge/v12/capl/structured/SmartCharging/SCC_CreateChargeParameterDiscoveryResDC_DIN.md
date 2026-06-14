# SCC_CreateChargeParameterDiscoveryResDC_DIN

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateChargeParameterDiscoveryResDC_DIN ( byte SessionID[], char ResponseCode[], long NotificationMaxDelay, char StatusCode[], char Notification[], long EVSEProcessing, float CurrentAndVoltageLimits[], float PeakCurrentRipple)
```

## Description

Creates a Charge Parameter Discovery Response message for sending, using the DC syntax.

## Return Values

1 if successful

## Availability

| Since Version |
|---|
