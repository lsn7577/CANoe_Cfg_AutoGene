# SCC_GetCostData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetCostData ( long i1, long i2, long i3, long i4, char CostKind[], dword& Amount, long& AmountMultiplier, long& HasMultiplier )
```

## Description

Gets the kind, amount and multiplier (range [-3..3]) values of the Cost element with the selected indices.

## Return Values

The kind, amount, and multiplier (range [-3..3]) values of the Cost element with the selected indices via references where the following applies:
To denote that the multiplier is not present, the flag HasMultiplier is set to 0.

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
