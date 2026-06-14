# SCC_GetSalesTariffEntryData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetSalesTariffEntryData ( long i1, long i2, long& Start, long& Duration, long& EPriceLevel, long& ConsumptionCostCount )
```

## Description

Gets the start time, duration, price level and the number of ConsumptionCost subelements of the SalesTariffEntry with the selected indices.

## Return Values

The start time, duration, price level and the number of ConsumptionCost subelements of the SalesTariffEntry with the selected indices via references, where the following applies:
If the optional element EPriceLevel is not present, a value of -1 is returned.

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
