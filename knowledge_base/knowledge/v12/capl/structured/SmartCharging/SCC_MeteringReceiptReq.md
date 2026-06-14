# SCC_MeteringReceiptReq

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_MeteringReceiptReq ( byte SessionID[], byte MessageSessionID[], long ScheduleTableEntryID )
```

## Description

The callback is called as soon as a Metering Receipt Request is received. With this request, the vehicle confirms receipt of the metering information sent by the charge point. Further details that are transmitted in this request can be queried with the helper function SCC_GetMeterInfoData

## Return Values

—

## Availability

| Since Version |
|---|
