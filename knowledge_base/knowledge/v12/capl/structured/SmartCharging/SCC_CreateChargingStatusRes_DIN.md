# SCC_CreateChargingStatusRes_DIN

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateChargingStatusRes_DIN ( byte SessionID[], char ResponseCode[], long NotificationMaxDelay, byte StatusFlags[], char Notification[], char EVSEID[], long SAScheduleTupleId, long ReceiptRequired )
```

## Description

Creates a Charging Status Response message for sending.

## Return Values

1 if successful

## Availability

| Since Version |
|---|
