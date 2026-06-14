# SCC_SetMaxCurrent

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetMaxCurrent ( float MaxCurrent )
```

## Description

Sets the limit for current. These limits are used in various messages for both AC and DC mode (the actual element name depends on the charging mode and the protocol version). Defaults can be set using the respective configuration file.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
