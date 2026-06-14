# SCC_GetPMaxScheduleEntryData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetPMaxScheduleEntryData ( long i1, long i2, long& Start, long& Duration, float& PMax )
```

## Description

Get various data of a PMaxScheduleEntry.

## Return Values

The start time, duration, and maximum power of the entry with the selected indices, where
If the optional element Duration is not present, a value of -1 is returned.

## Availability

| Since Version |
|---|
