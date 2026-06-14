# SCC_GetSalesTariffEntryData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetSalesTariffEntryData ( long i1, long i2, long& Start, long& Duration, long& EPriceLevel, long& ConsumptionCostCount )
```

## Description

Gets the start time, duration, price level and the number of ConsumptionCost subelements of the SalesTariffEntry with the selected indices.

## Return Values

The start time, duration, price level and the number of ConsumptionCost subelements of the SalesTariffEntry with the selected indices via references, where
If the optional element EPriceLevel is not present, a value of -1 is returned.

## Availability

| Since Version |
|---|
