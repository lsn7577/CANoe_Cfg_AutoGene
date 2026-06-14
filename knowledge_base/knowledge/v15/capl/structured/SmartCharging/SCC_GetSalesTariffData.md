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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | 3.0 SP3 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
