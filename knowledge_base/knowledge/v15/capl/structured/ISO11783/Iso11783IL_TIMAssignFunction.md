# Iso11783IL_TIMAssignFunction

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMAssignFunction(byte functionId, dbNode server); // form 1
long Iso11783IL_TIMAssignFunction(byte functionId, dbNode server, dword options); // form 2
long Iso11783IL_TIMAssignFunction(byte functionId, byte serverAddress); // form 3
long Iso11783IL_TIMAssignFunction(byte functionId, byte serverAddress, dword options); // form 4
long Iso11783IL_TIMAssignFunction(dbNode client, byte functionId, dbNode server); // form 5
long Iso11783IL_TIMAssignFunction(dbNode client, byte functionId, dbNode server, dword options); // form 6
long Iso11783IL_TIMAssignFunction(dbNode client, byte functionId, byte serverAddress); // form 7
long Iso11783IL_TIMAssignFunction(dbNode client, byte functionId, byte serverAddress, dword options); // form 8
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

| Name | Type | Description |
|---|---|---|
| Function ID |  | Description |
| 1-32 (1h-20h) |  | Auxiliary Value 1 – 32 |
| 64 (40h) |  | Front PTO |
| 65 (41h) |  | Rear PTO |
| 66 (42h) |  | Front hitch |
| 67 (43h) |  | Rear hitch |
| 68 (44h) |  | Vehicle speed |
| 70 (46h) |  | External guidance |
| server |  | The TIM client starts the function assignment procedure for the TIM function to the TIM server specified by this parameter. |
| serverAddress |  | The TIM client starts the function assignment procedure for the TIM function to the TIM server which uses this address. Value range: 0..253. |
| Option | Value | Meaning |
| Prevent assignment request | 01h | If the TIM client/server connection is already enabled by the operator the TIM_FunctionsAssignmentRequest is not sent at once. |
| client |  | TIM client node |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0: form 1, 2, 5, 6 11.0 SP2: form 3, 4, 7, 8 | 13.0 | — | — | 3.0: form 5, 6 3.0 SP2: form 7, 8 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 5, 6, 7, 8 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2, 3, 4) | ✔ (form 1, 2, 3, 4) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form form 5, 6, 7, 8) | ✔ (form form 5, 6, 7, 8) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form form 5, 6, 7, 8) | ✔ (form form 5, 6, 7, 8) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
