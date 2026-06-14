# SetThreshold9_16

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetThreshold9_16 (double Threshold);
```

## Description

Sets the threshold value for differentiating between high and low levels of the channels 9…16 of a digital module VT2516.There is only one threshold setting for all eight channels together.Voltages at the input exceeding this threshold value are evaluated as high level and voltages undershooting it are evaluated as low level.

## Return Values

0: Successful call

## Availability

| Since Version |
|---|
