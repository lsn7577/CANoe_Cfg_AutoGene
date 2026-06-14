# FRSSetBitstreamDist

> Category: `FRStress` | Type: `function`

## Syntax

```c
long FRSSetBitstreamDist (int triggerCondition, char disturbanceSequence[], int disturbanceLength, int delayAfterTrigger, int autoincrement);
```

## Description

Generates a bit sequence that is applied to the bus as a disturbance after the trigger is detected. In addition, a delay between the trigger and disturbance can be set. The autoincrement value increases the delay by the specified amount at each additional trigger.

## Return Values

0: successful

## Availability

| Since Version |
|---|
