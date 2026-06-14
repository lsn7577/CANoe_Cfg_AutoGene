# SCC_SLAC_SetToggleNum

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SLAC_SetToggleNum ( int ToggleNum )
```

## Description

Sets the number of toggles for the next CM_Validate.Cnf message. If this function is not used, either the value from the XML configuration or the default (2) is used.

The number of toggles is only applied to the second CM_Validate.Cnf in a validation sequence. The first one is specified to always have ToggleNum = 0.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
