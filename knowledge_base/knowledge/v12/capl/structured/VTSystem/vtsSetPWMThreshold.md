# vtsSetPWMThreshold

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetPWMThreshold (char Target[], double Threshold);
```

## Description

Sets the threshold value for differentiating between high and low levels.

Voltages at the input exceeding this threshold value are evaluated as high level and voltages undershooting it are evaluated as low level.

## Return Values

0: Successful call

## Availability

| Since Version |
|---|
