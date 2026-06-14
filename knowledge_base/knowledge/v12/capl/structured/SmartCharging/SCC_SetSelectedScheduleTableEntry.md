# SCC_SetSelectedScheduleTableEntry

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetSelectedScheduleTableEntry ( long ID )
```

## Description

Sets the ID of the selected SAScheduleTuple, which is sent in the messages PowerDeliveryReq and MeteringReceiptReq.

For a valid charge session, use one of the SAScheduleTupleIDs sent by the charge point in the message ChargeParameterDiscoveryRes. You can query them using the function SCC_GetSAScheduleTupleID. If no tuple is selected, the vehicle will automatically select the first or newest one.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
