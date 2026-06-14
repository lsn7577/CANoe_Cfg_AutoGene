# Iso11783IL_TIMUnassignFunction

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMUnassignFunction(byte functionId); // form 1
long Iso11783IL_TIMUnassignFunction(byte functionId, dword options); // form 2
long Iso11783IL_TIMUnassignFunction(dbNode client, byte functionId); // form 3
long Iso11783IL_TIMUnassignFunction(dbNode client, byte functionId, dword options); // form 4
```

## Description

If the TIM client is already authenticated and enabled by the operator then the assignment process with the function to be released is started again. By using parameter option you can prevent starting the assignment process.

If the TIM function is not assigned the this function removes the TIM function from the list of functions which shall be assigned to the TIM server.

To assign a TIM function you can use Iso11783IL_TIMAssignFunction.

## Parameters

| Name | Type | Description |
|---|---|---|
| Function ID |  | Description |
| 1-32 (1h-20h) |  | Auxiliary Value 1 – 32 |
| 64 (40h) |  | Front PTO |
| 65 (41h) |  | Rear PTO |
| 66 (42h) |  | Front hitch |
| 67 (43h) |  | Rear hitch |
| 68 (44h) |  | Vehicle speed |
| Option | Value | Description |
| Prevent assignment request | 01h | If the TIM client/server connection is already enabled by the operator the TIM_FunctionsAssignmentRequest is not sent at once. |
| client |  | TIM client node. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2, 3 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
