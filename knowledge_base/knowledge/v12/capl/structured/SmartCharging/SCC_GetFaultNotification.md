# SCC_GetFaultNotification

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_GetFaultNotification ( char FaultCode[], char FaultMsg[] )
```

## Description

Returns the fault code and fault message (optional) of the V2G message header.

## Return Values

0 if no fault code is contained in the V2G header

## Availability

| Since Version |
|---|
