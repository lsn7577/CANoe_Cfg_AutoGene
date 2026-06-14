# Iso11783IL_TIMConnectSysVarToFunctionState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMConnectSysVarToFunctionState(dword functionID, char[] sysVarNameWithPath); // form 1
long Iso11783IL_TIMConnectSysVarToFunctionState(dbNode participant, dword functionID, char[] sysVarNameWithPath); // form 2
```

## Description

Connects the automation state of a TIM function to a system variable.

If this function is used by a TIM client the system variable only changes if the TIM function is assigned by the client.

To release connection between the system variable and the function, just call the same method again, but with the empty string instead of the name of system variable.

You can also use the callback function Iso11783IL_TIMOnFunctionStateChanged if you are interested in the state of a function.

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
| participant | TIM participant (TIM server or TIM client). |
| sysVarNameWithPath | Name of the system variable, all name spaces inclusive. |

## Example

```c
Iso11783IL_TIMConnectSysVarToFunctionState(0, "sysvarAuxValve1State");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
