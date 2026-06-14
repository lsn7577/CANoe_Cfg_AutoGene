# SCC_CurrentDemandRes

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CurrentDemandRes ( byte SessionId[], long ResponseCode, float EVSEPresentVoltage, float EVSEPresentCurrent, byte LimitAchievedFlags[], char EVSEID[], long SAScheduleTupleID, long ReceiptRequired)
```

## Description

The callback is called as soon as a Current Demand Response is received. Further details that are transmitted in this message can be queried with

## Return Values

—

## Availability

| Since Version |
|---|
