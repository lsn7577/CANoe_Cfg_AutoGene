# SCC_SetSelectedService

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetSelectedService ( long ServiceID, long ParameterSetID )
```

## Description

Adds a service to the SelectedServiceList of the PaymentService- SelectionReq (former ServicePaymentSelectionReq) message.

For a correct message, use one of the ServiceIDs sent by the charge point in the message ServiceDiscoveryRes. The charge service is always selected automatically by the vehicle.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
