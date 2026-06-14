# Iso11783IL_TIMFunctionRequest

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMFunctionRequest(byte functionId, word requestValue); // form 1
long Iso11783IL_TIMFunctionRequest(byte functionId, word requestValue, long requestCounter); // form 2
long Iso11783IL_TIMFunctionRequest(dbNode client, byte functionId, word requestValue); // form 3
long Iso11783IL_TIMFunctionRequest(dbNode client, byte functionId, word requestValue, long requestCounter); // form 4
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
| requestValue | Requested raw value of the TIM function. |
| Value | Description |
| 0..13 | Valid counter value |
| 15 | Request counter is not used |
| -1 | Automatically increment the last use request counter value. If the last used request counter value is 15 then the request counter is not changed |
| client | TIM client node. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
