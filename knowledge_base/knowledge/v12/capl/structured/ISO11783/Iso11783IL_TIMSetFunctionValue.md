# Iso11783IL_TIMSetFunctionValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetFunctionValue(byte functionId, word rawValue); // form 1
```

## Description

Sets the value of a TIM function.

This value is transmitted in the status message of the TIM function.

## Parameters

| Name | Description |
|---|---|
| Function ID | Description |
| 1-32 (1h-20h) | Auxiliary Value 1 – 32 |
| 64 (40h) | Front PTO |
| 65 (41h) | Rear PTO |
| 66 (42h) | Front hitch |
| 67 (43h) | Rear hitch |
| 68 (44h) | Vehicle speed |
| 70 (46h) | External guidance |

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
