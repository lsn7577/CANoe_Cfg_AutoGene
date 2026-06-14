# SCC_SetReceiptRequired

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetReceiptRequired ( long ReceiptRequired )
```

## Description

Sets the flag ReceiptRequired, and adapts the simulation state to await a MeteringReceiptReq next. Although MeteringReceipt is a specific message for PnC mode, this is also possible when using EIM mode.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
