# SCC_SetPresentVoltage

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetPresentCurrent ( float PresentCurrent )
```

## Description

Sets the current voltage / current output for the respective connection. These values are used in various DC messages, and for the MeterInfo in AC mode. If no values are set, the charge point will automatically calculate defaults.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
