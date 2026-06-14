# Iso11783IL_TIMSetRequiredFacility

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetRequiredFacility(char facilityName[], long value); // form 1
```

## Description

Specifies if a TIM function facility is required by the TIM client or not.

After receiving the Functions Support Response message of the server the client checks if all defined required function facilities are supported by the server. If there are facilities that are not supported, the TIM Client terminates the automation.

You can use Iso11783IL_TIMResetAllRequiredFunctions to empty the list of necessary facilities.

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
