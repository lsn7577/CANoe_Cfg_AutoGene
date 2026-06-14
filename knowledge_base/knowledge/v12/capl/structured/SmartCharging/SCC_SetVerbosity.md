# SCC_SetVerbosity

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_SetVerbosity ( dword Level )
```

## Description

Sets the Verbosity parameter of the DLL. The higher the value is, the more information will be output in the write window.

## Parameters

| Name | Description |
|---|---|
| Selector | Description of return value |
| 0 | Signals only critical errors |
| 1 | Signals errors due to erroneous configurations, etc. |
| 2 | Warns, if an unexpected protocol status is reached, and signals missing obligatory callbacks |
| 3 | Informs about missing optional callbacks and minor problems |
| >3 | Signals low level events such as setting and expiring of timers |

## Return Values

—

## Availability

| Since Version |
|---|
