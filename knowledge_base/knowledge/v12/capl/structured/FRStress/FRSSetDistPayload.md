# FRSSetDistPayload

> Category: `FRStress` | Type: `function`

## Syntax

```c
long FRSSetDistPayload (int triggerCondition, int disturbancePayloadElement, int byteIndex, char disturbanceValue[]);
```

## Description

Modifies the Payload with bit accuracy. The disturbance is defined as a bit sequence. A complex disturbance can be configured through multiple calls.The associated trigger condition must not overlap with the disturbance.If the function is called in analog mode, it has no effect.

## Return Values

0: successful

## Availability

| Since Version |
|---|
