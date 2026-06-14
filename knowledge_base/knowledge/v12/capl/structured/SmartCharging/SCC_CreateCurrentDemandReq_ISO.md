# SCC_CreateCurrentDemandReq_ISO

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateCurrentDemandReq_ISO ( byte SessionID[], byte StatusFlags[], char ErrorCode[], float TargetVoltage, float TargetCurrent, long ChargingComplete )
```

## Description

Creates a Current Demand Request message for sending.

## Return Values

1 if successful

## Availability

| Since Version |
|---|
