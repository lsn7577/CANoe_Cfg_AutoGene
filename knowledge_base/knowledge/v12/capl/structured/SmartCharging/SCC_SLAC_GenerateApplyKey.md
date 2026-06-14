# SCC_SLAC_GenerateApplyKey

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SLAC_GenerateApplyKey ( )
```

## Description

Immediately sends a CM_Set_Key.Req message with a new NMK and NID. If a NMK is defined in the XML configuration file, this NMK is permanently discarded.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
