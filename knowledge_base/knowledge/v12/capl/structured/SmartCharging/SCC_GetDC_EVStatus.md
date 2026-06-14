# SCC_GetDC_EVStatus

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetDC_EVStatus ( long& EVReady, long& EVCabinConditioning, long& EVRESSConditioning, char EVErrorCode[], long& EVRESSSOC) // form 1
```

## Description

Gets the elements of DC_EVStatus (DIN/ISO) of a received DC message.

## Return Values

Returns the DC status bits of the vehicle and its error code, if contained in the message.

## Availability

| Since Version |
|---|
