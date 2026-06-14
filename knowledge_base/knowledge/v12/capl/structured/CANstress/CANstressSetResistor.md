# CANstressSetResistor

> Category: `CANstress` | Type: `function`

## Syntax

```c
void CANstressSetResistor (dword resId, float value);
```

## Description

Sets the value of a resistor for analog disturbances. This command will only take effect if permitted by the resistor layout set in the basic configuration. If the R_H layout is active, it will only be possible to set the RH resistor. If the CANstress device is inactive at this point, settings will only be applied once the CANstress device is active, i.e., once the trigger has been activated.

## Parameters

| Name | Description |
|---|---|
| 1 | for RH |
| 2 | for RSH |
| 3 | for RHL |
| 4 | for RSL |
| 5 | for RL |

## Return Values

—

## Availability

| Since Version |
|---|
