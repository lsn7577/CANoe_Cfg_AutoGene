# Iso11783IL_TIMAssignFunction

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMAssignFunction(byte functionId, dbNode server); // form 1
```

## Description

The function assigns a TIM function of the TIM client to a TIM server.

After receiving the TIM_FunctionsSupportResponse message of the server the client checks if:

a) the TIM function facilities added by this Iso11783IL_TIMSetRequiredFacility AND

b) the TIM functions assigned by this CAPL function

are supported by the server.

After the TIM client is successfully authenticated and enabled by the operator, it starts the assignment process f or all TIM functions which are configured by this CAPL function.

If the TIM client is already authenticated and enabled by the operator then the assignment process with the additional function ID to be assigned is started again. By using parameter option you can prevent starting the assignment process.

To release an assigned TIM function you can use Iso11783IL_TIMUnassingFunction.

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
