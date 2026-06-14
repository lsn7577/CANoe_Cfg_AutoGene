# SCC_SetProcessing

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetProcessing ( long Processing )
```

## Description

Sets the processing status of the charge point. This status is used for controlling various message loops, where the vehicle will continue sending the same request until EVSEProcessing is set to Finished within the response message.

The charge point will never send EVSEProcessing = Ongoing unless this function is called. The special value Ongoing_WaitingForCustomerInteraction of ISO IS will automatically be applied according to [V2G2-854] if EVSEProcessing was set to 1.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
