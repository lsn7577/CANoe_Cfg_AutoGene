# SetPWMThreshold

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetPWMThreshold (double Threshold);
```

## Description

Sets the threshold value for differentiating between high and low levels.

Voltages at the input exceeding this threshold value are evaluated as high level and voltages undershooting it are evaluated as low level.

## Parameters

| Name | Description |
|---|---|
| Comparison Table | VT1004 VT1004A VT1104 |
| Voltage value in volts in the range from ... | -32 V to +32 V -40 V to +40 V -60 V to +60 V |

## Return Values

0: Successful call

## Availability

| Since Version |
|---|
