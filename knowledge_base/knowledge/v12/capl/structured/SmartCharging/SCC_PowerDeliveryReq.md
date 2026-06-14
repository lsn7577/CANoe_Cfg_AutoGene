# SCC_PowerDeliveryReq

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_PowerDeliveryReq ( byte SessionId[], long ChargeProfileCount, long ChargeState, long ScheduleID)
```

## Description

The callback is called as soon as a Power Delivery Request is received.

With this request, the vehicle requests the charge point to switch on the current and to send the charging profile.

Further details that are transmitted in this request can be queried with

## Return Values

—

## Availability

| Since Version |
|---|
