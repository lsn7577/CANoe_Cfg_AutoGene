# SCC_GetServiceData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetServiceData ( long Index, long& ServiceID, char ServiceName[], char ServiceType[], char ServiceScope[], long& FreeService )
```

## Description

Get various elements of a service within a ServiceDiscoveryRes message.

## Return Values

ServiceName string (64 characters), ID, ServiceType, and ServiceScope string (32 characters) and FreeService flag with the specified list index < ServiceCount. When using a recent protocol version, an index of 0 refers to the element ChargeService.

## Availability

| Since Version |
|---|
