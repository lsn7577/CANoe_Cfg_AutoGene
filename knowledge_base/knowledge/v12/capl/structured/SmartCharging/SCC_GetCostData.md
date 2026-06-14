# SCC_GetCostData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetCostData ( long i1, long i2, long i3, long i4, char CostKind[], dword& Amount, long& AmountMultiplier, long& HasMultiplier )
```

## Description

Gets the kind, amount and multiplier (range [-3..3]) values of the Cost element with the selected indices.

## Return Values

The kind, amount and multiplier (range [-3..3]) values of the Cost element with the selected indices via references, where
To denote that the multiplier is not present, the flag HasMultiplier is set to 0.

## Availability

| Since Version |
|---|
