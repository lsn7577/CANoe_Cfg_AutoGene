# Iso11783IL_TIMSetSupportedFacility

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetSupportedFacility(char functionFacilityName[], long value); // form 1
```

## Description

The function sets a facility of a TIM function in a TIM server.

By means of this function you can define all possible TIM functions supported by the TIM server.

If least one facility of a function is set then the function is listed in the TIM_FunctionsSupportResponse message. By default the other facilities of the function are set to value 3 (not available).

You can use Iso11783IL_TIMResetAllSupportedFunctions to remove all functions and all of their facilities. Then they are no longer listed in the TIM_FunctionsSupportResponse message.

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
