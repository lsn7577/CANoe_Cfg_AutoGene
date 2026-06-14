# SCC_SetShutdownRequest

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetShutdownRequest ( long ShutdownRequest )
```

## Description

Demands the stop of the charging session from the vehicle, the appropriate mechanism for the active schema version, or withdraws this request.

You can still initiate a shutdown using the specific parameter of the target schema version instead of using this convenience function.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
