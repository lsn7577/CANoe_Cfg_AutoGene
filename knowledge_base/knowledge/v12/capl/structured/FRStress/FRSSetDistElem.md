# FRSSetDistElem

> Category: `FRStress` | Type: `function`

## Syntax

```c
long FRSSetDistElem (int triggerCondition, int disturbanceElement, int disturbanceValue);
```

## Description

Modifies the specified frame element with bit accuracy. A complex disturbance can be configured through multiple calls.

The associated trigger condition must not overlap with the disturbance.

If the function is called in analog mode, it has no effect.

## Return Values

0: successful

## Availability

| Since Version |
|---|
