# Iso11783IL_TIMUnassignFunction

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMUnassignFunction(byte functionId); // form 1
```

## Description

If the TIM client is already authenticated and enabled by the operator then the assignment process with the function to be released is started again. By using parameter option you can prevent starting the assignment process.

If the TIM function is not assigned the this function removes the TIM function from the list of functions which shall be assigned to the TIM server.

To assign a TIM function you can use Iso11783IL_TIMAssignFunction.

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

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
