# SCC_GetSalesTariffData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetSalesTariffData ( long Index, char IdAttr[], long& SalesTariffId, char Description, long& NumEPriceLevels )
```

## Description

Gets various elements of the Sales Tariff within the SAScheduleTuple with the selected index.

## Return Values

ID attribute, SalesTariffId, Description and number of distinct price levels of the SalesTariff within the SAScheduleTuple with the selected index. If no SalesTariff is present, SalesTariffId is set to -1. This can be used to check the present of a SalesTariff in a SAScheduleTuple.

## Availability

| Since Version |
|---|
