# Iso11783IL_TIMFunctionRequest

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMFunctionRequest(byte functionId, word requestValue); // form 1
```

## Description

The function sends a function request value to the TIM server to control a TIM function.

The function fails if the TIM function is not assigned to the TIM client.

By default, the request counter is set to 15 (request counter is not used).

If the property useRequestCounter (see Iso11783IL_TIMSetProperty) is set to 1 then the counter is incremented each time the request value for this function is sent (up to value 13, then start with 0 again).

You can use form 2 to set the request counter directly.

The function value request is sent with a maximum repetition rate of 100 ms even this CAPL function is called more frequently.

The last request value is transmitted with repetition rate 2000 ms periodically if this function is not called.

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
