# SCC_CreateCurrentDemandRes_DIN

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateCurrentDemandRes_DIN ( byte SessionID[], char ResponseCode[], long NotificationMaxDelay, char StatusCode[], char Notification[], float PresentVoltage, float PresentCurrent, byte LimitAchievedFlags[] )
```

## Description

Creates a Current Demand Request message for sending.

## Return Values

1 if successful

## Availability

| Since Version |
|---|
